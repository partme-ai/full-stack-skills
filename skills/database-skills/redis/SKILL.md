---
name: redis
description: Provides comprehensive guidance for Redis including data structures, commands, pub/sub, persistence, clustering, and caching patterns. Use when the user asks about Redis, needs to use Redis for caching, implement Redis data structures, or work with Redis features.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 使用 Redis 数据结构（string、hash、list、set、sorted set）与命令
- 配置持久化（RDB/AOF）、主从、集群与客户端连接
- 实现缓存、会话、限流、队列等模式

## How to use this skill

1. **命令**：GET/SET、HGETALL、LPUSH、SADD、ZRANGE；过期 TTL/EXPIRE；Lua 脚本。
2. **CLI/驱动**：redis-cli；各语言驱动（连接池、序列化）；Redis Stack 扩展（搜索、JSON）。
3. **环境**：单机、哨兵或集群；内存与持久化策略；生产注意密码与网络。

## Best Practices

- 键命名规范与 TTL 避免堆积；大 key 拆分或压缩。
- 持久化与主从按可用性需求选择；集群分片与扩容规划。
- 监控内存与慢查询；安全加固与备份策略。

## Keywords

redis, cache, 缓存, 数据结构, 主从, 集群
