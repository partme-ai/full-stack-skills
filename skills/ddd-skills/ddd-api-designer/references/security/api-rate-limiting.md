# API 限流设计

差异化限流策略：
- Command API：50 req/s（写操作成本高）
- Query API：200 req/s（读操作可放宽）
- Auth API：10 req/s（防暴力破解）
- 全局：1000 req/s

实现方式：令牌桶算法（Token Bucket），支持突发流量。
限流响应：429 Too Many Requests + Retry-After header。
