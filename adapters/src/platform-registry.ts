import os from 'node:os';
import path from 'node:path';

export type InstallMode = 'copy-or-link';

export interface PlatformRecord {
  id: string;
  aliases: string[];
  displayName: string;
  projectPath: string;
  globalPath: string;
  installMode: InstallMode;
  notes?: string;
}

const home = os.homedir();
const configHome = process.env.XDG_CONFIG_HOME?.trim() || path.join(home, '.config');
const codexHome = process.env.CODEX_HOME?.trim() || path.join(home, '.codex');
const claudeHome = process.env.CLAUDE_CONFIG_DIR?.trim() || path.join(home, '.claude');

const sharedAgentsProjectPath = '.agents/skills';
const sharedAgentsGlobalPath = path.join(configHome, 'agents', 'skills');

export const platformRegistry: PlatformRecord[] = [
  { id: 'amp', aliases: [], displayName: 'Amp', projectPath: sharedAgentsProjectPath, globalPath: sharedAgentsGlobalPath, installMode: 'copy-or-link' },
  { id: 'kimi-cli', aliases: [], displayName: 'Kimi Code CLI', projectPath: sharedAgentsProjectPath, globalPath: sharedAgentsGlobalPath, installMode: 'copy-or-link' },
  { id: 'replit', aliases: [], displayName: 'Replit', projectPath: sharedAgentsProjectPath, globalPath: sharedAgentsGlobalPath, installMode: 'copy-or-link' },
  { id: 'universal', aliases: [], displayName: 'Universal', projectPath: sharedAgentsProjectPath, globalPath: sharedAgentsGlobalPath, installMode: 'copy-or-link' },
  { id: 'antigravity', aliases: [], displayName: 'Antigravity', projectPath: sharedAgentsProjectPath, globalPath: path.join(home, '.gemini', 'antigravity', 'skills'), installMode: 'copy-or-link' },
  { id: 'augment', aliases: [], displayName: 'Augment', projectPath: '.augment/skills', globalPath: path.join(home, '.augment', 'skills'), installMode: 'copy-or-link' },
  { id: 'claude-code', aliases: ['claude'], displayName: 'Claude Code', projectPath: '.claude/skills', globalPath: path.join(claudeHome, 'skills'), installMode: 'copy-or-link' },
  { id: 'openclaw', aliases: [], displayName: 'OpenClaw', projectPath: 'skills', globalPath: path.join(home, '.openclaw', 'skills'), installMode: 'copy-or-link' },
  { id: 'cline', aliases: [], displayName: 'Cline', projectPath: sharedAgentsProjectPath, globalPath: sharedAgentsGlobalPath, installMode: 'copy-or-link' },
  { id: 'warp', aliases: [], displayName: 'Warp', projectPath: sharedAgentsProjectPath, globalPath: sharedAgentsGlobalPath, installMode: 'copy-or-link' },
  { id: 'codebuddy', aliases: [], displayName: 'CodeBuddy', projectPath: '.codebuddy/skills', globalPath: path.join(home, '.codebuddy', 'skills'), installMode: 'copy-or-link' },
  { id: 'codex', aliases: [], displayName: 'Codex', projectPath: sharedAgentsProjectPath, globalPath: path.join(codexHome, 'skills'), installMode: 'copy-or-link' },
  { id: 'command-code', aliases: [], displayName: 'Command Code', projectPath: '.commandcode/skills', globalPath: path.join(home, '.commandcode', 'skills'), installMode: 'copy-or-link' },
  { id: 'continue', aliases: [], displayName: 'Continue', projectPath: '.continue/skills', globalPath: path.join(home, '.continue', 'skills'), installMode: 'copy-or-link' },
  { id: 'cortex', aliases: [], displayName: 'Cortex Code', projectPath: '.cortex/skills', globalPath: path.join(home, '.snowflake', 'cortex', 'skills'), installMode: 'copy-or-link' },
  { id: 'crush', aliases: [], displayName: 'Crush', projectPath: '.crush/skills', globalPath: path.join(configHome, 'crush', 'skills'), installMode: 'copy-or-link' },
  { id: 'cursor', aliases: [], displayName: 'Cursor', projectPath: sharedAgentsProjectPath, globalPath: path.join(home, '.cursor', 'skills'), installMode: 'copy-or-link' },
  { id: 'deepagents', aliases: ['deep-agents'], displayName: 'Deep Agents', projectPath: sharedAgentsProjectPath, globalPath: path.join(home, '.deepagents', 'agent', 'skills'), installMode: 'copy-or-link' },
  { id: 'droid', aliases: [], displayName: 'Droid', projectPath: '.factory/skills', globalPath: path.join(home, '.factory', 'skills'), installMode: 'copy-or-link' },
  { id: 'gemini-cli', aliases: [], displayName: 'Gemini CLI', projectPath: sharedAgentsProjectPath, globalPath: path.join(home, '.gemini', 'skills'), installMode: 'copy-or-link' },
  { id: 'github-copilot', aliases: ['copilot'], displayName: 'GitHub Copilot', projectPath: sharedAgentsProjectPath, globalPath: path.join(home, '.copilot', 'skills'), installMode: 'copy-or-link' },
  { id: 'goose', aliases: [], displayName: 'Goose', projectPath: '.goose/skills', globalPath: path.join(configHome, 'goose', 'skills'), installMode: 'copy-or-link' },
  { id: 'junie', aliases: [], displayName: 'Junie', projectPath: '.junie/skills', globalPath: path.join(home, '.junie', 'skills'), installMode: 'copy-or-link' },
  { id: 'iflow-cli', aliases: [], displayName: 'iFlow CLI', projectPath: '.iflow/skills', globalPath: path.join(home, '.iflow', 'skills'), installMode: 'copy-or-link' },
  { id: 'kilo', aliases: [], displayName: 'Kilo Code', projectPath: '.kilocode/skills', globalPath: path.join(home, '.kilocode', 'skills'), installMode: 'copy-or-link' },
  { id: 'kiro-cli', aliases: [], displayName: 'Kiro CLI', projectPath: '.kiro/skills', globalPath: path.join(home, '.kiro', 'skills'), installMode: 'copy-or-link' },
  { id: 'kode', aliases: [], displayName: 'Kode', projectPath: '.kode/skills', globalPath: path.join(home, '.kode', 'skills'), installMode: 'copy-or-link' },
  { id: 'mcpjam', aliases: [], displayName: 'MCPJam', projectPath: '.mcpjam/skills', globalPath: path.join(home, '.mcpjam', 'skills'), installMode: 'copy-or-link' },
  { id: 'mistral-vibe', aliases: ['vibe'], displayName: 'Mistral Vibe', projectPath: '.vibe/skills', globalPath: path.join(home, '.vibe', 'skills'), installMode: 'copy-or-link' },
  { id: 'mux', aliases: [], displayName: 'Mux', projectPath: '.mux/skills', globalPath: path.join(home, '.mux', 'skills'), installMode: 'copy-or-link' },
  { id: 'opencode', aliases: [], displayName: 'OpenCode', projectPath: sharedAgentsProjectPath, globalPath: path.join(configHome, 'opencode', 'skills'), installMode: 'copy-or-link' },
  { id: 'openhands', aliases: [], displayName: 'OpenHands', projectPath: '.openhands/skills', globalPath: path.join(home, '.openhands', 'skills'), installMode: 'copy-or-link' },
  { id: 'pi', aliases: [], displayName: 'Pi', projectPath: '.pi/skills', globalPath: path.join(home, '.pi', 'agent', 'skills'), installMode: 'copy-or-link' },
  { id: 'qoder', aliases: [], displayName: 'Qoder', projectPath: '.qoder/skills', globalPath: path.join(home, '.qoder', 'skills'), installMode: 'copy-or-link' },
  { id: 'qwen-code', aliases: [], displayName: 'Qwen Code', projectPath: '.qwen/skills', globalPath: path.join(home, '.qwen', 'skills'), installMode: 'copy-or-link' },
  { id: 'roo', aliases: [], displayName: 'Roo Code', projectPath: '.roo/skills', globalPath: path.join(home, '.roo', 'skills'), installMode: 'copy-or-link' },
  { id: 'trae', aliases: [], displayName: 'Trae', projectPath: '.trae/skills', globalPath: path.join(home, '.trae', 'skills'), installMode: 'copy-or-link' },
  { id: 'trae-cn', aliases: [], displayName: 'Trae CN', projectPath: '.trae/skills', globalPath: path.join(home, '.trae-cn', 'skills'), installMode: 'copy-or-link' },
  { id: 'windsurf', aliases: [], displayName: 'Windsurf', projectPath: '.windsurf/skills', globalPath: path.join(home, '.codeium', 'windsurf', 'skills'), installMode: 'copy-or-link' },
  { id: 'zencoder', aliases: [], displayName: 'Zencoder', projectPath: '.zencoder/skills', globalPath: path.join(home, '.zencoder', 'skills'), installMode: 'copy-or-link' },
  { id: 'neovate', aliases: [], displayName: 'Neovate', projectPath: '.neovate/skills', globalPath: path.join(home, '.neovate', 'skills'), installMode: 'copy-or-link' },
  { id: 'pochi', aliases: [], displayName: 'Pochi', projectPath: '.pochi/skills', globalPath: path.join(home, '.pochi', 'skills'), installMode: 'copy-or-link' },
  { id: 'adal', aliases: [], displayName: 'AdaL', projectPath: '.adal/skills', globalPath: path.join(home, '.adal', 'skills'), installMode: 'copy-or-link' }
];

const registryMap = new Map<string, PlatformRecord>();

for (const platform of platformRegistry) {
  registryMap.set(platform.id, platform);
  for (const alias of platform.aliases) {
    registryMap.set(alias, platform);
  }
}

export function resolvePlatform(input: string): PlatformRecord {
  const resolved = registryMap.get(input);
  if (!resolved) {
    throw new Error(`Unsupported platform: ${input}`);
  }
  return resolved;
}

export function getPlatformProjectPath(platform: PlatformRecord, projectRoot: string): string {
  return path.join(projectRoot, platform.projectPath);
}

export function formatDisplayPath(targetPath: string): string {
  return targetPath.startsWith(home) ? targetPath.replace(home, '~') : targetPath;
}

export function renderPlatformTableMarkdown(): string {
  const lines = [
    '| Platform | ID / Aliases | Project Path | Global Path |',
    '|---|---|---|---|'
  ];
  for (const platform of platformRegistry) {
    const aliases = [platform.id, ...platform.aliases].join(', ');
    lines.push(
      `| ${platform.displayName} | \`${aliases}\` | \`${platform.projectPath}/\` | \`${formatDisplayPath(platform.globalPath)}/\` |`
    );
  }
  return lines.join('\n');
}
