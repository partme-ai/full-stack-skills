#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema, Tool, } from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
// Define the path to marketplace.json
// Assuming structure: full-stack-skills/skills/skill-installer/index.ts
// Marketplace: full-stack-skills/.claude-plugin/marketplace.json
const MARKETPLACE_PATH = path.resolve(__dirname, "../../.claude-plugin/marketplace.json");
// Quick hack: The current marketplace.json only lists paths.
// We will simulate a "Rich Marketplace" by reading the SKILL.md of each referenced skill.
const server = new Server({
    name: "skill-installer",
    version: "1.0.0",
}, {
    capabilities: {
        tools: {},
    },
});
async function getMarketplaceSkills() {
    try {
        const data = await fs.readFile(MARKETPLACE_PATH, "utf-8");
        const marketplace = JSON.parse(data);
        // The current marketplace.json has a "skills" array of strings (paths)
        // We need to resolve these paths to get names and descriptions from SKILL.md or package.json
        const skillsList = [];
        for (const skillPath of marketplace.skills) {
            // skillPath is like "./skills/skill-creator"
            // Resolve absolute path
            const absoluteSkillPath = path.resolve(path.dirname(MARKETPLACE_PATH), skillPath);
            try {
                // Try reading SKILL.md
                const skillMdPath = path.join(absoluteSkillPath, "SKILL.md");
                const skillMdContent = await fs.readFile(skillMdPath, "utf-8");
                // Extract name and description from SKILL.md (naively)
                // Usually SKILL.md starts with # Name\n\n> Description
                const lines = skillMdContent.split("\n");
                let name = path.basename(skillPath);
                let description = "No description available";
                for (const line of lines) {
                    if (line.startsWith("# ")) {
                        name = line.substring(2).trim();
                    }
                    else if (line.trim().length > 0 && !line.startsWith("#") && description === "No description available") {
                        // First non-header line is description
                        description = line.trim();
                    }
                }
                skillsList.push({
                    name,
                    description,
                    path: skillPath
                });
            }
            catch (e) {
                console.error(`Failed to read metadata for ${skillPath}`, e);
            }
        }
        return skillsList;
    }
    catch (error) {
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
                description: "Install a skill from the marketplace",
                inputSchema: {
                    type: "object",
                    properties: {
                        skill_name: {
                            type: "string",
                            description: "The exact name or path of the skill to install",
                        },
                    },
                    required: ["skill_name"],
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
            const results = skills.filter((s) => s.name.toLowerCase().includes(query) ||
                s.description.toLowerCase().includes(query));
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
            const skillName = String(request.params.arguments?.skill_name);
            // In a real implementation, this would run `npm install` or register the MCP server config
            // For now, we return a success message simulating the action
            return {
                content: [
                    {
                        type: "text",
                        text: `Successfully installed skill: ${skillName}. \n\n(Note: This is a simulation. In a real environment, this would configure the MCP client to load the new server.)`,
                    },
                ],
            };
        }
        case "list_installed_skills": {
            // Mock installed skills
            return {
                content: [
                    {
                        type: "text",
                        text: JSON.stringify([
                            { name: "skill-installer", version: "1.0.0" },
                            { name: "skill-sop-creator", version: "1.0.0" }
                        ], null, 2)
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
//# sourceMappingURL=index.js.map