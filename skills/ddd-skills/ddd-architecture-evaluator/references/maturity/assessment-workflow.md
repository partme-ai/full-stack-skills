# Maturity Assessment Workflow

## Preparation
1. Collect sample code from each layer (Controller/Service/Domain/Infrastructure)
2. Pull architecture documentation (ADR, C4 diagrams) 
3. Interview 2-3 team members about DDD understanding
4. Run automated scans (ArchUnit, JDepend) for metrics

## Assessment Session
1. Per-level checklist evaluation (30 min)
2. Score calculation with evidence
3. Gap analysis: current vs target
4. Timeline estimation for each level progression

## Common Assessment Traps
- **Confirmation bias**: Looking for evidence that confirms expected level
- **Recency effect**: Judging based on recently refactored modules, ignoring rest
- **Scale blindness**: A small project at L3 is different from an enterprise at L3
