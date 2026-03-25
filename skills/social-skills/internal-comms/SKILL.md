---
name: internal-comms
description: "Draft internal company communications including 3P updates, newsletters, FAQ responses, status reports, leadership updates, incident reports, and project updates using company-standard formats. Use when the user asks to write internal communications, draft status reports, create newsletters, prepare leadership updates, or compose any company-wide messaging."
license: Complete terms in LICENSE.txt
---

# Internal Communications Writer

Draft polished internal company communications using standardized formats for consistent, professional messaging.

## Workflow

1. **Identify communication type** from the user's request:
   - 3P updates (Progress, Plans, Problems)
   - Company newsletters
   - FAQ responses
   - Status reports or leadership updates
   - Incident reports or project updates

2. **Load the matching guideline** from the `examples/` directory:
   - `examples/3p-updates.md` - Progress/Plans/Problems team updates
   - `examples/company-newsletter.md` - Company-wide newsletters
   - `examples/faq-answers.md` - Frequently asked questions
   - `examples/general-comms.md` - Other communication types

3. **Gather context** from the user:
   - Key updates, metrics, or decisions to communicate
   - Target audience and desired tone
   - Any deadlines or distribution channels

4. **Draft the communication** following the guideline's format, then iterate based on feedback.

### Example: 3P Update

```markdown
## Progress
- Shipped v2.1 authentication module ahead of schedule
- Completed API migration for 3 downstream services

## Plans
- Begin load testing for Q3 launch (target: 10k concurrent users)
- Finalize design review for notification system

## Problems
- CI pipeline flakiness causing 15% build failure rate — investigating root cause
```

If the communication type doesn't match any existing guideline, ask for clarification about the desired format.

## Keywords

3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms, status report, leadership update, incident report
