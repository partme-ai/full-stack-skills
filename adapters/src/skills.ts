import fs from 'node:fs/promises';
import path from 'node:path';

const IGNORED_DIR_NAMES = new Set(['__pycache__']);
const IGNORED_FILE_NAMES = new Set(['.DS_Store']);
const EXCLUDED_SKILL_DIRECTORIES = new Set([path.join('skills', 'pencil-skills', 'docs')]);

export interface SkillEntry {
  name: string;
  group: string;
  dir: string;
  relativeDir: string;
  skillFile: string;
}

export interface AuditReport {
  skillsDir: string;
  skillCount: number;
  missingSkillDirectories: string[];
  excludedDirectories: string[];
  platformCount: number;
}

async function pathExists(targetPath: string): Promise<boolean> {
  try {
    await fs.access(targetPath);
    return true;
  } catch {
    return false;
  }
}

function isExcludedSkillDirectory(relativeDir: string): boolean {
  return EXCLUDED_SKILL_DIRECTORIES.has(relativeDir);
}

export async function resolveSkillsRoot(input?: string): Promise<string> {
  const direct = input ? path.resolve(input) : path.resolve(process.cwd(), '..', 'skills');
  if (await pathExists(direct)) {
    return direct;
  }
  const fromRepoRoot = path.resolve(process.cwd(), 'skills');
  if (await pathExists(fromRepoRoot)) {
    return fromRepoRoot;
  }
  throw new Error(`Unable to locate skills directory. Checked: ${direct} and ${fromRepoRoot}`);
}

export async function discoverSkillEntries(skillsDirInput?: string): Promise<SkillEntry[]> {
  const skillsDir = await resolveSkillsRoot(skillsDirInput);
  const groups = await fs.readdir(skillsDir, { withFileTypes: true });
  const entries: SkillEntry[] = [];

  for (const group of groups) {
    if (!group.isDirectory() || IGNORED_DIR_NAMES.has(group.name) || group.name.startsWith('.')) {
      continue;
    }
    const groupDir = path.join(skillsDir, group.name);
    const skillCandidates = await fs.readdir(groupDir, { withFileTypes: true });
    for (const candidate of skillCandidates) {
      if (!candidate.isDirectory() || IGNORED_DIR_NAMES.has(candidate.name) || candidate.name.startsWith('.')) {
        continue;
      }
      const absoluteDir = path.join(groupDir, candidate.name);
      const relativeDir = path.relative(path.dirname(skillsDir), absoluteDir);
      if (isExcludedSkillDirectory(relativeDir)) {
        continue;
      }
      const skillFile = path.join(absoluteDir, 'SKILL.md');
      if (!(await pathExists(skillFile))) {
        continue;
      }
      entries.push({
        name: candidate.name,
        group: group.name,
        dir: absoluteDir,
        relativeDir,
        skillFile
      });
    }
  }

  return entries.sort((left, right) => left.relativeDir.localeCompare(right.relativeDir));
}

export async function findMissingSkillDirectories(skillsDirInput?: string): Promise<string[]> {
  const skillsDir = await resolveSkillsRoot(skillsDirInput);
  const groups = await fs.readdir(skillsDir, { withFileTypes: true });
  const missing: string[] = [];

  for (const group of groups) {
    if (!group.isDirectory() || IGNORED_DIR_NAMES.has(group.name) || group.name.startsWith('.')) {
      continue;
    }
    const groupDir = path.join(skillsDir, group.name);
    const skillCandidates = await fs.readdir(groupDir, { withFileTypes: true });
    for (const candidate of skillCandidates) {
      if (!candidate.isDirectory() || candidate.name.startsWith('.') || IGNORED_DIR_NAMES.has(candidate.name)) {
        continue;
      }
      const absoluteDir = path.join(groupDir, candidate.name);
      const relativeDir = path.relative(path.dirname(skillsDir), absoluteDir);
      if (isExcludedSkillDirectory(relativeDir)) {
        continue;
      }
      const skillFile = path.join(absoluteDir, 'SKILL.md');
      if (!(await pathExists(skillFile))) {
        missing.push(relativeDir);
      }
    }
  }
  return missing.sort();
}

export async function copySkillDirectory(sourceDir: string, destinationDir: string): Promise<void> {
  await fs.mkdir(destinationDir, { recursive: true });
  const items = await fs.readdir(sourceDir, { withFileTypes: true });

  for (const item of items) {
    if (IGNORED_FILE_NAMES.has(item.name) || IGNORED_DIR_NAMES.has(item.name) || item.name.startsWith('.')) {
      continue;
    }
    const source = path.join(sourceDir, item.name);
    const destination = path.join(destinationDir, item.name);

    if (item.isDirectory()) {
      await copySkillDirectory(source, destination);
      continue;
    }

    if (item.isFile()) {
      await fs.copyFile(source, destination);
    }
  }
}

export async function createAuditReport(skillsDirInput: string | undefined, platformCount: number): Promise<AuditReport> {
  const skillsDir = await resolveSkillsRoot(skillsDirInput);
  const skillEntries = await discoverSkillEntries(skillsDir);
  const missing = await findMissingSkillDirectories(skillsDir);

  return {
    skillsDir,
    skillCount: skillEntries.length,
    missingSkillDirectories: missing,
    excludedDirectories: Array.from(EXCLUDED_SKILL_DIRECTORIES.values()).sort(),
    platformCount
  };
}
