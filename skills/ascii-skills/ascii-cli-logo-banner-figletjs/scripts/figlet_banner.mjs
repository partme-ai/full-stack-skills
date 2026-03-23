#!/usr/bin/env node
import process from "node:process";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

process.stdout.on("error", (err) => {
  if (err && err.code === "EPIPE") {
    process.exit(0);
  }
  throw err;
});

function parseArgs(argv) {
  const args = {
    brand: null,
    version: null,
    repo: null,
    docs: null,
    author: null,
    width: 80,
    slogan: null,
    hint: null,
    font: "Standard",
    horizontalLayout: "default",
    verticalLayout: "default",
    whitespaceBreak: true,
    center: true,
    rule: true,
    colorMode: "none",
    colorStart: 33,
    colorEnd: 129,
  };

  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    const next = argv[i + 1];
    if (a === "--brand" && next) {
      args.brand = next;
      i++;
      continue;
    }
    if (a === "--version" && next) {
      args.version = next;
      i++;
      continue;
    }
    if (a === "--repo" && next) {
      args.repo = next;
      i++;
      continue;
    }
    if (a === "--docs" && next) {
      args.docs = next;
      i++;
      continue;
    }
    if (a === "--author" && next) {
      args.author = next;
      i++;
      continue;
    }
    if (a === "--width" && next) {
      args.width = Number.parseInt(next, 10);
      i++;
      continue;
    }
    if (a === "--slogan" && next) {
      args.slogan = next;
      i++;
      continue;
    }
    if (a === "--hint" && next) {
      args.hint = next;
      i++;
      continue;
    }
    if (a === "--colorMode" && next) {
      args.colorMode = next;
      i++;
      continue;
    }
    if (a === "--colorStart" && next) {
      args.colorStart = Number.parseInt(next, 10);
      i++;
      continue;
    }
    if (a === "--colorEnd" && next) {
      args.colorEnd = Number.parseInt(next, 10);
      i++;
      continue;
    }
    if (a === "--font" && next) {
      args.font = next;
      i++;
      continue;
    }
    if (a === "--horizontalLayout" && next) {
      args.horizontalLayout = next;
      i++;
      continue;
    }
    if (a === "--verticalLayout" && next) {
      args.verticalLayout = next;
      i++;
      continue;
    }
    if (a === "--whitespaceBreak" && next) {
      args.whitespaceBreak = next === "true";
      i++;
      continue;
    }
    if (a === "--center") {
      args.center = true;
      continue;
    }
    if (a === "--no-center") {
      args.center = false;
      continue;
    }
    if (a === "--rule") {
      args.rule = true;
      continue;
    }
    if (a === "--no-rule") {
      args.rule = false;
      continue;
    }
    if (a === "--help" || a === "-h") {
      args.help = true;
      continue;
    }
  }
  return args;
}

function hr(width, ch = "-") {
  const c = (ch && ch.length > 0 ? ch[0] : "-");
  return c.repeat(Math.max(0, width));
}

function centerLine(line, width) {
  const s = String(line ?? "").replace(/\n/g, "").trimEnd();
  if (width <= 0) return "";
  if (s.length >= width) return s.slice(0, width).trimEnd();
  const padLeft = Math.floor((width - s.length) / 2);
  return " ".repeat(padLeft) + s;
}

function ansiFg256(code) {
  return `\x1b[38;5;${code}m`;
}

function ansiReset() {
  return "\x1b[0m";
}

function lerp(a, b, t) {
  return Math.round(a + (b - a) * t);
}

function colorizeAnsi256Line(line, start, end) {
  const reset = ansiReset();
  const s = String(line ?? "");
  const maxLen = Math.max(1, s.length);
  let out = "";
  for (let x = 0; x < s.length; x++) {
    const ch = s[x];
    if (ch === " ") {
      out += ch;
      continue;
    }
    const t = maxLen <= 1 ? 0 : x / (maxLen - 1);
    const code = lerp(start, end, t);
    out += ansiFg256(code) + ch + reset;
  }
  return out;
}

function compactBanner(args) {
  const title = args.version ? `${args.brand} (v${args.version})` : args.brand;
  const lines = [title.slice(0, args.width)];
  if (args.slogan) lines.push(centerLine(args.slogan, args.width));
  if (args.hint) lines.push(centerLine(args.hint, args.width));
  if (args.rule) {
    lines.push(hr(args.width, "-"));
    if (args.repo) lines.push(`Repo: ${args.repo}`.slice(0, args.width));
    if (args.docs) lines.push(`Docs: ${args.docs}`.slice(0, args.width));
    if (args.author) lines.push(`Author: ${args.author}`.slice(0, args.width));
  }
  return lines.join("\n").trimEnd();
}

async function loadFiglet() {
  try {
    const mod = await import("figlet");
    return mod.default ?? mod;
  } catch {
    const require = createRequire(import.meta.url);
    const here = path.dirname(fileURLToPath(import.meta.url));
    const repoRoot = path.resolve(here, "../../../..");
    const candidatePaths = [
      process.cwd(),
      repoRoot,
      path.join(repoRoot, "partme-cli-ts"),
      here,
    ];
    try {
      const resolved = require.resolve("figlet", { paths: candidatePaths });
      const mod = require(resolved);
      return mod.default ?? mod;
    } catch {
      throw new Error(
        "Missing dependency: figlet (npm). Install with: npm install figlet (or provide it via partme-cli-ts/node_modules)."
      );
    }
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || !args.brand) {
    process.stdout.write(
      [
        "Usage:",
        "  node scripts/figlet_banner.mjs --brand <NAME> [options]",
        "",
        "Options:",
        "  --version <v>             Optional version",
        "  --repo <url>              Repo URL",
        "  --docs <url>              Docs URL",
        "  --author <name>           Author/team",
        "  --width <n>               Banner width (default 80)",
        "  --slogan <text>           Centered slogan line under the logo",
        "  --hint <text>             Centered hint line under the slogan",
        "  --no-rule                 Hero output (logo + centered lines only)",
        "  --no-center               Do not center-align logo/slogan/hint",
        "  --colorMode <mode>        none|ansi256 (logo only)",
        "  --colorStart <n>          ANSI 256 start color (0-255, default 33)",
        "  --colorEnd <n>            ANSI 256 end color (0-255, default 129)",
        "  --font <name>             FIGlet font (default Standard)",
        "  --horizontalLayout <val>  default|full|fitted|controlled smushing|universal smushing",
        "  --verticalLayout <val>    default|full|fitted|controlled smushing|universal smushing",
        "  --whitespaceBreak <bool>  true|false (default true)",
        "",
        "Install dependency:",
        "  npm install figlet",
        "",
      ].join("\n")
    );
    process.exit(args.brand ? 0 : 1);
  }

  const width = Number.isFinite(args.width) ? Math.max(10, args.width) : 80;
  args.width = width;
  if (width < 60) {
    process.stdout.write(compactBanner(args) + "\n");
    return;
  }

  const figlet = await loadFiglet();
  const logo = figlet.textSync(args.brand, {
    font: args.font,
    horizontalLayout: args.horizontalLayout,
    verticalLayout: args.verticalLayout,
    width: args.width,
    whitespaceBreak: args.whitespaceBreak,
  });

  const lines = [];
  const rawLogoLines = logo.trimEnd().split("\n");
  const colorMode = args.colorMode === "ansi256" ? "ansi256" : "none";
  const colorStart = Number.isFinite(args.colorStart) ? Math.max(0, Math.min(255, args.colorStart)) : 33;
  const colorEnd = Number.isFinite(args.colorEnd) ? Math.max(0, Math.min(255, args.colorEnd)) : 129;

  if (args.center) {
    for (const l of rawLogoLines) {
      const centered = centerLine(l, args.width);
      lines.push(colorMode === "ansi256" ? colorizeAnsi256Line(centered, colorStart, colorEnd) : centered);
    }
  } else {
    const joined = rawLogoLines.join("\n").trimEnd();
    if (colorMode === "ansi256") {
      for (const l of joined.split("\n")) lines.push(colorizeAnsi256Line(l, colorStart, colorEnd));
    } else {
      lines.push(joined);
    }
  }

  if (args.slogan || args.hint) lines.push("");
  if (args.slogan) lines.push(args.center ? centerLine(args.slogan, args.width) : String(args.slogan));
  if (args.hint) {
    lines.push("");
    lines.push(args.center ? centerLine(args.hint, args.width) : String(args.hint));
  }

  if (args.rule) {
    lines.push("");
    lines.push(hr(args.width, "-"));
    lines.push(`Name: ${args.brand}`.slice(0, args.width));
    if (args.version) lines.push(`Version: ${args.version}`.slice(0, args.width));
    if (args.author) lines.push(`Author: ${args.author}`.slice(0, args.width));
    if (args.repo) lines.push(`Repo: ${args.repo}`.slice(0, args.width));
    if (args.docs) lines.push(`Docs: ${args.docs}`.slice(0, args.width));
  }

  process.stdout.write(lines.join("\n").trimEnd() + "\n");
}

main().catch((err) => {
  process.stderr.write(`Error: ${err?.message ?? String(err)}\n`);
  process.exit(1);
});
