import fs from 'node:fs/promises';
import path from 'node:path';
import {
  formatDisplayPath,
  getPlatformProjectPath,
  platformRegistry,
  renderPlatformTableMarkdown,
  resolvePlatform,
  type PlatformRecord
} from './platform-registry.js';
import {
  copySkillDirectory,
  createAuditReport,
  discoverSkillEntries,
  resolveSkillsRoot,
  type SkillEntry
} from './skills.js';

export interface ParsedOptions {
  positional: string[];
  flags: Map<string, string[]>;
}

export interface ConvertOptions {
  platform: string;
  output?: string;
  skillsDir?: string;
  dryRun: boolean;
  selectedSkills: string[];
}

export interface InstallOptions {
  platform: string;
  scope: 'project' | 'global';
  projectRoot: string;
  skillsDir?: string;
  dryRun: boolean;
  link: boolean;
  selectedSkills: string[];
  target?: string;
}

export function parseArgv(argv: string[]): ParsedOptions {
  const positional: string[] = [];
  const flags = new Map<string, string[]>();

  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (!token.startsWith('--')) {
      positional.push(token);
      continue;
    }

    const [flagName, inlineValue] = token.split('=', 2);
    if (inlineValue !== undefined) {
      flags.set(flagName, [...(flags.get(flagName) || []), inlineValue]);
      continue;
    }

    const nextToken = argv[index + 1];
    if (nextToken && !nextToken.startsWith('--')) {
      flags.set(flagName, [...(flags.get(flagName) || []), nextToken]);
      index += 1;
      continue;
    }

    flags.set(flagName, [...(flags.get(flagName) || []), 'true']);
  }

  return { positional, flags };
}

function getFlagValue(options: ParsedOptions, flag: string, fallback?: string): string | undefined {
  return options.flags.get(flag)?.at(-1) || fallback;
}

function getFlagValues(options: ParsedOptions, flag: string): string[] {
  return options.flags.get(flag) || [];
}

function hasFlag(options: ParsedOptions, flag: string): boolean {
  return options.flags.has(flag);
}

function filterSkillEntries(entries: SkillEntry[], selectedSkills: string[]): SkillEntry[] {
  if (selectedSkills.length === 0) {
    return entries;
  }
  const wanted = new Set(selectedSkills);
  return entries.filter((entry) => wanted.has(entry.name) || wanted.has(entry.relativeDir));
}

async function ensureRemoved(targetPath: string): Promise<void> {
  await fs.rm(targetPath, { recursive: true, force: true });
}

async function ensureParentDir(targetPath: string): Promise<void> {
  await fs.mkdir(path.dirname(targetPath), { recursive: true });
}

function printJson(data: unknown): void {
  console.log(JSON.stringify(data, null, 2));
}

export function buildConvertOptions(parsed: ParsedOptions): ConvertOptions {
  const platform = getFlagValue(parsed, '--platform', 'all');
  if (!platform) {
    throw new Error('Missing --platform value.');
  }
  return {
    platform,
    output: getFlagValue(parsed, '--output'),
    skillsDir: getFlagValue(parsed, '--skills-dir'),
    dryRun: hasFlag(parsed, '--dry-run'),
    selectedSkills: getFlagValues(parsed, '--skill')
  };
}

export function buildInstallOptions(parsed: ParsedOptions): InstallOptions {
  const platform = getFlagValue(parsed, '--platform', 'universal') || 'universal';
  const scope = getFlagValue(parsed, '--scope', 'project');
  if (scope !== 'project' && scope !== 'global') {
    throw new Error(`Unsupported --scope value: ${scope}`);
  }
  return {
    platform,
    scope,
    projectRoot: path.resolve(
      getFlagValue(parsed, '--project-root', process.env.INIT_CWD || process.cwd()) ||
        process.env.INIT_CWD ||
        process.cwd()
    ),
    skillsDir: getFlagValue(parsed, '--skills-dir'),
    dryRun: hasFlag(parsed, '--dry-run'),
    link: hasFlag(parsed, '--link'),
    selectedSkills: getFlagValues(parsed, '--skill'),
    target: getFlagValue(parsed, '--target')
  };
}

export async function runPlatformsCommand(parsed: ParsedOptions): Promise<void> {
  if (hasFlag(parsed, '--json')) {
    printJson(platformRegistry);
    return;
  }

  if (hasFlag(parsed, '--markdown')) {
    console.log(renderPlatformTableMarkdown());
    return;
  }

  console.log(`Supported platforms: ${platformRegistry.length}`);
  for (const platform of platformRegistry) {
    const aliases = platform.aliases.length > 0 ? ` (${platform.aliases.join(', ')})` : '';
    console.log(
      `- ${platform.displayName} [${platform.id}${aliases}] -> project: ${platform.projectPath}/ | global: ${formatDisplayPath(platform.globalPath)}/`
    );
  }
}

export async function runAuditCommand(parsed: ParsedOptions): Promise<void> {
  const report = await createAuditReport(getFlagValue(parsed, '--skills-dir'), platformRegistry.length);

  if (hasFlag(parsed, '--json')) {
    printJson(report);
    return;
  }

  console.log(`Skills root: ${report.skillsDir}`);
  console.log(`Convertible skills: ${report.skillCount}`);
  console.log(`Supported platforms: ${report.platformCount}`);
  console.log(`Excluded directories: ${report.excludedDirectories.join(', ')}`);
  if (report.missingSkillDirectories.length === 0) {
    console.log('Missing SKILL.md directories: none');
    return;
  }
  console.log(`Missing SKILL.md directories (${report.missingSkillDirectories.length}):`);
  for (const entry of report.missingSkillDirectories) {
    console.log(`- ${entry}`);
  }
}

async function convertForPlatform(platform: PlatformRecord, options: ConvertOptions): Promise<void> {
  const skillsDir = await resolveSkillsRoot(options.skillsDir);
  const outputRoot = path.resolve(options.output || path.join('..', 'adapters-output'));
  const entries = filterSkillEntries(await discoverSkillEntries(skillsDir), options.selectedSkills);
  const targetRoot = path.join(outputRoot, platform.id, platform.projectPath);

  if (options.dryRun) {
    console.log(`[dry-run] ${platform.id} -> ${targetRoot}`);
    for (const entry of entries) {
      console.log(`  - ${entry.relativeDir} => ${path.join(targetRoot, entry.name)}`);
    }
    return;
  }

  await fs.mkdir(targetRoot, { recursive: true });
  for (const entry of entries) {
    const destination = path.join(targetRoot, entry.name);
    await ensureRemoved(destination);
    await copySkillDirectory(entry.dir, destination);
  }
  console.log(`Converted ${entries.length} skills for ${platform.id} -> ${targetRoot}`);
}

export async function runConvertCommand(parsed: ParsedOptions): Promise<void> {
  const options = buildConvertOptions(parsed);
  const platforms = options.platform === 'all' ? platformRegistry : [resolvePlatform(options.platform)];
  for (const platform of platforms) {
    await convertForPlatform(platform, options);
  }
}

async function installSkillEntry(
  entry: SkillEntry,
  targetRoot: string,
  dryRun: boolean,
  link: boolean
): Promise<void> {
  const destination = path.join(targetRoot, entry.name);
  if (dryRun) {
    console.log(`[dry-run] ${entry.relativeDir} => ${destination}`);
    return;
  }

  await ensureParentDir(destination);
  await ensureRemoved(destination);
  if (link) {
    await fs.symlink(entry.dir, destination, 'dir');
    return;
  }
  await copySkillDirectory(entry.dir, destination);
}

export async function runInstallCommand(parsed: ParsedOptions): Promise<void> {
  const options = buildInstallOptions(parsed);
  const platform = resolvePlatform(options.platform);
  const entries = filterSkillEntries(await discoverSkillEntries(options.skillsDir), options.selectedSkills);
  const targetRoot = options.target
    ? path.resolve(options.target)
    : options.scope === 'global'
      ? platform.globalPath
      : getPlatformProjectPath(platform, options.projectRoot);

  if (!options.dryRun) {
    await fs.mkdir(targetRoot, { recursive: true });
  }

  for (const entry of entries) {
    await installSkillEntry(entry, targetRoot, options.dryRun, options.link);
  }

  const action = options.link ? 'Linked' : 'Installed';
  console.log(`${action} ${entries.length} skills for ${platform.id} (${options.scope}) -> ${formatDisplayPath(targetRoot)}`);
}

export function printHelp(): void {
  console.log(`fskill

Usage:
  fskill platforms [--json|--markdown]
  fskill audit [--skills-dir <path>] [--json]
  fskill convert --platform <id|all> [--skills-dir <path>] [--output <path>] [--skill <name>]... [--dry-run]
  fskill install [--platform <id>] [--scope project|global] [--project-root <path>] [--skills-dir <path>] [--target <path>] [--skill <name>]... [--link] [--dry-run]
  fskill version

Defaults:
  fskill install               -> installs to .agents/skills/ under the current project
  fskill install --scope global -> installs to ~/.config/agents/skills/

Examples:
  fskill platforms
  fskill audit --json
  fskill convert --platform all --output ./adapters-output
  fskill convert --platform claude-code --output ./adapters-output
  fskill install
  fskill install --platform antigravity --scope global
  fskill install --platform codex --scope global --skill react --skill vue3
`);
}
