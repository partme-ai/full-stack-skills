---
name: redis
description: "Guides Redis usage including data structures (strings, hashes, lists, sets, sorted sets), caching patterns, pub/sub, persistence (RDB/AOF), clustering, and Lua scripting. Use when the user needs to implement caching, session storage, rate limiting, queues, or any Redis-based data layer."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Use Redis data structures (string, hash, list, set, sorted set) and commands
- Implement caching, session storage, rate limiting, or message queues with Redis
- Configure persistence (RDB/AOF), replication, Sentinel, or Redis Cluster
- Write Lua scripts for atomic Redis operations
- Connect via redis-cli or language drivers (connection pooling, serialization)

## How to use this skill

### Workflow

1. **Identify the use case** - Caching, session store, queue, pub/sub, or data structure
2. **Choose the data structure** - String for simple values, Hash for objects, List for queues, Sorted Set for rankings
3. **Implement with appropriate commands** - Use the patterns below
4. **Configure persistence and replication** - Based on durability requirements

### Quick-Start Example: Caching with TTL

```bash
# Set a cache entry with 5-minute TTL
redis-cli SET user:1001:profile '{"name":"Alice","role":"admin"}' EX 300

# Retrieve the cached value
redis-cli GET user:1001:profile

# Check remaining TTL
redis-cli TTL user:1001:profile
```

### Rate Limiting with Sorted Sets

```bash
# Add request timestamp to sorted set
redis-cli ZADD rate:user:1001 1710000000 "req1"

# Count requests in the last 60 seconds
redis-cli ZRANGEBYSCORE rate:user:1001 1709999940 1710000000

# Remove expired entries
redis-cli ZREMRANGEBYSCORE rate:user:1001 0 1709999940
```

## Best Practices

1. **Use namespaced keys** - Format as `service:entity:id:field` (e.g., `app:user:1001:session`)
2. **Always set TTL** - Prevent memory leaks from stale data; use `EX`/`PX` on SET
3. **Avoid large keys** - Split hashes over 1MB; use SCAN instead of KEYS in production
4. **Choose persistence wisely** - RDB for snapshots (fast restart), AOF for durability (every write)
5. **Secure production** - Require password (`requirepass`), bind to private IPs, disable `FLUSHALL`

## Keywords

redis, cache, caching, 缓存, data structures, 数据结构, pub/sub, sentinel, cluster, 主从, 集群, rate limiting, session store, Lua scripting
