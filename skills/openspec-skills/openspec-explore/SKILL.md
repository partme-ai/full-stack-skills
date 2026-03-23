---
name: openspec-explore
description: Think through ideas, investigate problems, and clarify requirements before committing to a change using `/opsx:explore`. Use when the user says "explore an idea", "think through this", "investigate options", or wants to brainstorm before creating a formal change.
---

# OpenSpec Explore Skill

Use **`/opsx:explore`** to think through ideas, investigate problems, compare options, and clarify requirements — all without creating any artifacts or committing to a structure. When insights crystallize, transition to **openspec-new** or **openspec-ff**.

## When to Use

- Requirements are unclear and the user needs to investigate first.
- Comparing multiple approaches before deciding on one.
- The user wants to explore the codebase for improvement opportunities.
- Brainstorming before a formal change proposal.

## Prerequisites

- **OpenSpec initialized** in the project (see **openspec-initial**).

## Workflow

1. **Start exploration**
   - Run `/opsx:explore` or `/opsx:explore [topic]`.
   - The agent opens an exploratory conversation with no structure required.

2. **Investigate**
   - Analyze the codebase, compare options, create diagrams, answer questions.
   - No artifacts are created during exploration — it is purely a thinking exercise.

3. **Transition when ready**
   - When the user has clarity, suggest `/opsx:new <change-name>` to start a formal change.
   - Or `/opsx:ff <change-name>` if they want to create all planning artifacts at once.

## Outputs

- No artifacts or files are created. The output is the conversation itself — insights, options, recommendations.

## Next Steps

- When ready to act: use **openspec-new** to start a change, or **openspec-ff** to fast-forward through planning.

## Troubleshooting

- **"Commands not recognized"**: Ensure OpenSpec is initialized (`openspec init`). See **openspec-initial**.

## References

- [OpenSpec Commands: /opsx:explore](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
