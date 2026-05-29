# Redis ZSet 排行榜示例

## 游戏排行榜 (Go)

```go
package redis

import (
    "context"
    "github.com/redis/go-redis/v9"
)

type Leaderboard struct {
    rdb *redis.Client
    key string
}

func NewLeaderboard(rdb *redis.Client, gameID string) *Leaderboard {
    return &Leaderboard{rdb: rdb, key: "leaderboard:" + gameID}
}

// AddScore 增加玩家分数 (原子操作)
func (lb *Leaderboard) AddScore(ctx context.Context, player string, score float64) error {
    return lb.rdb.ZIncrBy(ctx, lb.key, score, player).Err()
}

// GetTopN 获取前 N 名
func (lb *Leaderboard) GetTopN(ctx context.Context, n int64) ([]redis.Z, error) {
    return lb.rdb.ZRevRangeWithScores(ctx, lb.key, 0, n-1).Result()
}

// GetRank 获取玩家排名 (从 0 开始)
func (lb *Leaderboard) GetRank(ctx context.Context, player string) (int64, error) {
    rank, err := lb.rdb.ZRevRank(ctx, lb.key, player).Result()
    if err != nil {
        return -1, err
    }
    return rank + 1, nil // 转为 1-based
}

// GetScore 获取玩家分数
func (lb *Leaderboard) GetScore(ctx context.Context, player string) (float64, error) {
    return lb.rdb.ZScore(ctx, lb.key, player).Result()
}
```

## 周榜 + 日榜 + 总榜设计

```redis
# 命名规范
leaderboard:total          # 总榜 (长周期)
leaderboard:2024:W01       # 周榜
leaderboard:2024:01:15     # 日榜

# 每日零点：创建新日榜
# 每周一零点：创建新周榜

# 合并多期分数 (ZUNIONSTORE)
ZUNIONSTORE leaderboard:month 3
    leaderboard:2024:01:01 leaderboard:2024:01:02 leaderboard:2024:01:03
    WEIGHTS 1 1 1
    AGGREGATE SUM
```
