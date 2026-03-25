---
name: documentation-builder
description: "Generates structured technical documentation including API docs (OpenAPI/Swagger), README files, user guides, developer guides, and changelogs. Use when the user needs to create or improve project documentation, generate API reference docs, write onboarding guides, or structure documentation for a codebase."
---

## When to use this skill

Use this skill whenever the user wants to:
- Generate a project README with installation, usage, and contributing sections
- Create API documentation from code or OpenAPI specs
- Write developer onboarding or setup guides
- Build user manuals or quick-start tutorials
- Structure documentation for a new or existing project
- Generate a CHANGELOG from commit history or release notes

## How to use this skill

### Workflow

1. **Identify the doc type** - README, API reference, user guide, developer guide, or changelog
2. **Gather context** - Read the codebase, existing docs, and project structure
3. **Generate documentation** - Use the templates and patterns below
4. **Validate** - Ensure all code examples run, links resolve, and sections are complete

### README Template

```markdown
# Project Name

Brief description of what the project does and why it exists.

## Quick Start

\`\`\`bash
npm install my-package
\`\`\`

\`\`\`typescript
import { MyClient } from 'my-package';
const client = new MyClient({ apiKey: process.env.API_KEY });
const result = await client.query('hello');
\`\`\`

## Features

- Feature one with brief explanation
- Feature two with brief explanation

## Installation

Detailed installation steps for different environments.

## Usage

Detailed usage examples with code snippets.

## API Reference

Link to full API docs or inline reference.

## Contributing

How to contribute, run tests, and submit PRs.

## License

License type and link.
```

### API Documentation Pattern (OpenAPI)

```yaml
paths:
  /users/{id}:
    get:
      summary: Get user by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
```

## Best Practices

1. **Start with a quick-start** - Let readers get running in under 2 minutes
2. **Include runnable code examples** - Every API endpoint or function should have a copy-paste example
3. **Keep docs next to code** - Co-locate documentation with the source it describes
4. **Use consistent structure** - Follow the same heading hierarchy across all doc pages
5. **Version your docs** - Tag documentation alongside code releases

## Keywords

文档编写, documentation, README, API docs, OpenAPI, Swagger, user guide, 用户手册, developer guide, 开发指南, changelog, 技术文档
