# Redis Stream 消息队列示例

## 1. 生产-消费模式

```redis
# 生产者: 发送消息
XADD orders * order_id 1001 user_id 42 amount 99.99 status pending
XADD orders * order_id 1002 user_id 55 amount 199.00 status pending

# 消费者: 读取消息 (非阻塞)
XRANGE orders - + COUNT 10

# 消费者: 阻塞读取新消息
XREAD COUNT 1 BLOCK 5000 STREAMS orders $

# 消息长度
XLEN orders

# 删除消息
XDEL orders 1700000000000-0

# 修剪 (保留最近的 1000 条)
XTRIM orders MAXLEN ~ 1000
```

## 2. 消费组模式

```redis
# 创建消费组 (从最新消息开始消费)
XGROUP CREATE orders payment-group $ MKSTREAM
XGROUP CREATE orders inventory-group $
XGROUP CREATE orders notification-group $

# 消费组成员: 读取未确认消息
# payment-service
XREADGROUP GROUP payment-group worker-1 COUNT 1 BLOCK 2000 STREAMS orders >
# inventory-service
XREADGROUP GROUP inventory-group worker-1 COUNT 1 BLOCK 2000 STREAMS orders >
# notification-service
XREADGROUP GROUP notification-group worker-1 COUNT 1 BLOCK 2000 STREAMS orders >

# 确认消费 (ACK)
XACK orders payment-group 1700000000000-0

# 查看待确认消息
XPENDING orders payment-group

# 查看消费组信息
XINFO GROUPS orders
XINFO CONSUMERS orders payment-group
```

## 3. CAP 对比: Stream vs Kafka

| 特性 | Redis Stream | Apache Kafka |
|------|-------------|-------------|
| 延迟 | <1ms | <10ms |
| 消息持久化 | RDB/AOF | 磁盘日志 |
| 消息回溯 | 支持 | 支持 |
| 消费组 | 支持 | 支持 |
| 分区顺序 | 单分区有序 | 单分区有序 |
| 数据保留 | 内存+磁盘 (可控) | 磁盘 (可配置) |
| 吞吐量 | 10万+/s | 百万+/s |
| 运维复杂度 | 低 (Redis 原生) | 高 (需 ZK) |
| 适用场景 | 微服务异步、任务队列 | 大数据流、日志采集 |
