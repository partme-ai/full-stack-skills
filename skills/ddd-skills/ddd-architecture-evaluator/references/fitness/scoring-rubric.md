# Fitness Scoring Rubric — Detailed Criteria

## Business Alignment

| Context | Over-engineered | Just right | Under-engineered |
|---------|:---------------:|:----------:|:----------------:|
| Simple CRUD | Clean/Hexagonal | N-tier / MVC | — |
| Medium complexity | Microservices | DDD Layered / Onion | N-tier / MVC |
| Complex domain | — | Hexagonal / Clean | DDD Layered |
| High-scale | — | Event-driven + CQRS | Monolith DDD |

## Scoring Calibration

- **Score 5**: Architecture enables business agility. New features are easy to add.
- **Score 4**: Minor friction. Some adaptation needed.
- **Score 3**: Architecture does not actively help or hinder.
- **Score 2**: Architecture creates noticeable friction.
- **Score 1**: Architecture is a blocker. Major rework needed.
