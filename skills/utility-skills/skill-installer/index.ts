#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  type Tool,
} from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Define the path to marketplace.json
// Assuming structure: full-stack-skills/skills/skill-installer/index.ts
// Marketplace: full-stack-skills/.claude-plugin/marketplace.json
// From dist/index.js:
// .. -> skill-installer
// .. -> skills
// .. -> full-stack-skills
const MARKETPLACE_PATH = path.resolve(__dirname, "../../../.claude-plugin/marketplace.json");
const INSTALLED_SKILLS_PATH = path.resolve(__dirname, "../installed_skills.json");

interface Skill {
  name: string;
  description: string;
  path: string;
  installed_at?: string;
}

interface Marketplace {
  plugins: {
    skills: string[];
  }[];
}

const server = new Server(
  {
    name: "skill-installer",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function getInstalledSkills(): Promise<Skill[]> {
  try {
    const data = await fs.readFile(INSTALLED_SKILLS_PATH, "utf-8");
    return JSON.parse(data) as Skill[];
  } catch (error) {
    // If file doesn't exist, return empty array
    return [];
  }
}

async function saveInstalledSkill(skill: Skill): Promise<void> {
  const currentSkills = await getInstalledSkills();
  // Check if already installed
  if (!currentSkills.some(s => s.path === skill.path)) {
    skill.installed_at = new Date().toISOString();
    currentSkills.push(skill);
    await fs.writeFile(INSTALLED_SKILLS_PATH, JSON.stringify(currentSkills, null, 2));
  }
}

async function getMarketplaceSkills(): Promise<Skill[]> {
  try {
    const data = await fs.readFile(MARKETPLACE_PATH, "utf-8");
    const marketplace = JSON.parse(data) as Marketplace;
    
    const skillsList: Skill[] = [];
    
    if (marketplace.plugins) {
      for (const plugin of marketplace.plugins) {
        if (plugin.skills) {
          for (const skillPath of plugin.skills) {
            // skillPath is like "./skills/vue2"
            // Resolve absolute path relative to project root (parent of .claude-plugin)
            const projectRoot = path.resolve(path.dirname(MARKETPLACE_PATH), "..");
            const absoluteSkillPath = path.resolve(projectRoot, skillPath);
            
            try {
              // Try reading SKILL.md
              const skillMdPath = path.join(absoluteSkillPath, "SKILL.md");
              // Check if file exists first to avoid throwing too many errors
              try {
                  await fs.access(skillMdPath);
              } catch {
                  continue;
              }

              const skillMdContent = await fs.readFile(skillMdPath, "utf-8");
              
              // Extract name and description from SKILL.md.
              // 1) If file has YAML frontmatter (--- ... ---), parse name/description from it and use first non-# line after --- as fallback for description (Trae/simple-parser compliance).
              // 2) Otherwise use first # line as name and first non-# line as description.
              const lines = skillMdContent.split("\n");
              let name = path.basename(skillPath);
              let description = "No description available";
              let bodyStartIndex = 0;
              const fmMatch = skillMdContent.match(/^---\s*\n([\s\S]*?)\n---\s*\n/);
              if (fmMatch) {
                bodyStartIndex = fmMatch[0].split("\n").length;
                const fm = fmMatch[1];
                const nameM = fm.match(/^name:\s*(.+)$/m);
                const descM = fm.match(/^description:\s*(.+)$/m);
                if (nameM) name = nameM[1].trim().replace(/^["']|["']$/g, "");
                if (descM) description = descM[1].trim().replace(/^["']|["']$/g, "");
              }
              for (let i = bodyStartIndex; i < lines.length; i++) {
                const line = lines[i];
                if (line.startsWith("# ")) {
                  name = line.substring(2).trim();
                }
                if (description === "No description available" && line.trim().length > 0 && !line.startsWith("#")) {
                  description = line.trim();
                  break;
                }
              }
              
              skillsList.push({
                name,
                description,
                path: skillPath
              });
              
            } catch (e) {
              console.error(`Failed to read metadata for ${skillPath}`, e);
            }
          }
        }
      }
    }
    
    return skillsList;
    
  } catch (error) {
    console.error("Failed to read marketplace.json", error);
    return [];
  }
}

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "search_skills",
        description: "Search for available AI skills in the PartMe marketplace",
        inputSchema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "Search query (e.g., 'finance', 'image generation')",
            },
          },
          required: ["query"],
        },
      },
      {
        name: "install_skill",
        description: "Install a skill from the marketplace. This will verify the skill exists and register it as installed.",
        inputSchema: {
          type: "object",
          properties: {
            skill_path: {
              type: "string",
              description: "The path of the skill to install (e.g., './skills/vue2')",
            },
          },
          required: ["skill_path"],
        },
      },
      {
        name: "list_installed_skills",
        description: "List currently installed skills",
        inputSchema: {
          type: "object",
          properties: {},
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  switch (request.params.name) {
    case "search_skills": {
      const query = String(request.params.arguments?.query).toLowerCase();
      const skills = await getMarketplaceSkills();
      
      const results = skills.filter(
        (s) =>
          s.name.toLowerCase().includes(query) ||
          s.description.toLowerCase().includes(query)
      );

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(results, null, 2),
          },
        ],
      };
    }

    case "install_skill": {
      const skillPath = String(request.params.arguments?.skill_path);
      const skills = await getMarketplaceSkills();
      const skillToInstall = skills.find(s => s.path === skillPath);
      
      if (!skillToInstall) {
         return {
            content: [
               {
                 type: "text",
                 text: `Error: Skill with path '${skillPath}' not found in marketplace.`
               }
            ],
            isError: true
         };
      }
      
      await saveInstalledSkill(skillToInstall);
      
      return {
        content: [
          {
            type: "text",
            text: `Successfully installed skill: ${skillToInstall.name} (${skillToInstall.path}).\n\nSkill Description: ${skillToInstall.description}\n\nNote: For knowledge skills, you can now ask questions about this topic. For executable skills, they are now registered.`,
          },
        ],
      };
    }

    case "list_installed_skills": {
        const installedSkills = await getInstalledSkills();
        return {
            content: [
                {
                    type: "text",
                    text: JSON.stringify(installedSkills, null, 2),
                }
            ]
        };
    }

    default:
      throw new Error("Unknown tool");
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
