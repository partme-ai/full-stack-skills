# Strangler Fig Migration — Detailed Planning

## Phase Breakdown

| Phase | Activity | Duration | Success Criteria |
|-------|----------|:--------:|------------------|
| **Wrap** | Add ACL around legacy | 1-2 weeks | New code calls ACL, not legacy directly |
| **Replace** | Implement core feature in new system | 2-6 weeks | Feature parity with legacy |
| **Route** | Route traffic to new implementation | 1-2 weeks | 100% of traffic goes to new system |
| **Remove** | Delete legacy code | 1 week | Zero legacy references remain |

## Migration Decision Tree

```
Want to migrate?
├─ Is business value clear?
│  ├─ Yes → Proceed with Strangler Fig
│  └─ No → Don't migrate; document decision
├─ Team capacity available?
│  ├─ Yes → Start with lowest-risk module
│  └─ No → Hire or pause; don't half-migrate
├─ Data migration needed?
│  ├─ Yes → Plan dual-write + validation
│  └─ No → Simpler cutover
```

## Rollback Checklist

```
☐ Feature flag to switch traffic
☐ Dual-write to legacy DB until validated
☐ Data integrity comparison script
☐ Performance baseline recorded
☐ Max rollback time: 4 hours
```
