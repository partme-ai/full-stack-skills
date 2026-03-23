#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  parseArgv,
  printHelp,
  runAuditCommand,
  runConvertCommand,
  runInstallCommand,
  runPlatformsCommand
} from './commands.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const packageJsonPath = path.resolve(__dirname, '..', 'package.json');
const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8')) as { version?: string };

async function main(): Promise<void> {
  const [command, ...rest] = process.argv.slice(2);

  if (!command || command === 'help' || command === '--help' || command === '-h') {
    printHelp();
    return;
  }

  if (command === '--version' || command === '-v' || command === 'version') {
    console.log(packageJson.version || '0.0.0');
    return;
  }

  const parsed = parseArgv(rest);

  switch (command) {
    case 'platforms':
      await runPlatformsCommand(parsed);
      return;
    case 'audit':
      await runAuditCommand(parsed);
      return;
    case 'convert':
      await runConvertCommand(parsed);
      return;
    case 'install':
      await runInstallCommand(parsed);
      return;
    default:
      throw new Error(`Unknown command: ${command}`);
  }
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Error: ${message}`);
  process.exitCode = 1;
});
