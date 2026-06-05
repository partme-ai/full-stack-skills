# DDD Architecture Comparison Reference

## Quick Decision Matrix

| Dimension | Layered | Onion | Hexagonal | Clean | COLA |
|-----------|:--:|:--:|:--:|:--:|:--:|
| **Learning Cost** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★☆ |
| **Business Complexity Fit** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★★ |
| **CRUD Efficiency** | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | ★★☆ |
| **Infrastructure Replaceability** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★☆ |
| **Test Friendliness** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★★ |
| **Chinese Community** | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | ★★★ |
| **Code Generation Support** | Good | Poor | Poor | Poor | Excellent |
| **Team Size Fit** | 1-5 | 5-15 | 5-15 | 15-50 | 5-50 |
| **Origin** | Martin Fowler | Jeffrey Palermo 2008 | Alistair Cockburn 2005 | Robert C. Martin 2012 | Alibaba 2018 |

## Architecture Selection Flowchart

```
What is the team size?
├── 1-5 people
│   └── Business complexity?
│       ├── Simple CRUD → LAYERED
│       ├── Moderate → COLA Simplified
│       └── Complex → COLA (single module)
│
├── 5-15 people
│   └── Technology stack?
│       ├── Spring Boot + MyBatis/Chinese ecosystem → COLA
│       ├── Domain purity is top priority → HEXAGONAL
│       └── Infrastructure needs frequent swapping → HEXAGONAL / ONION
│
└── 15-50 people
    └── Organization type?
        ├── Chinese enterprise → COLA (multi-module)
        ├── International/English-first → CLEAN
        └── Mixed → HEXAGONAL per service + COLA per module
```

## Architecture Selection by Scenario

| Scenario | Recommended | Why |
|----------|-------------|-----|
| REST API + Simple CRUD | Layered | Minimal overhead |
| Core domain logic heavy | Hexagonal / Onion | Best domain isolation |
| Chinese enterprise backend | COLA | Ecosystem + Chinese docs |
| Multi-entry (REST+CLI+MQ+gRPC) | Hexagonal | Cleanest adapter isolation |
| Strict module boundaries needed | Clean | Physical module isolation |
| Frequent DB/MQ changes | Hexagonal / Onion | Easy adapter swap |
| Rapid prototyping → Production | Layered → COLA | Progressive evolution |
| Microservice internal standard | Hexagonal + COLA | Best of both worlds |
