# JSONB 查询示例

## 场景：电商用户配置系统

本示例演示如何使用 JSONB 存储和查询用户偏好配置。

## 建表与数据

```sql
-- 建表
CREATE TABLE user_configs (
    id      BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    config  JSONB NOT NULL DEFAULT '{}'
);

-- 插入示例数据
INSERT INTO user_configs (user_id, config) VALUES
(1, '{
    "theme": "dark",
    "notifications": {"email": true, "sms": false, "push": true},
    "preferences": {"language": "zh-CN", "timezone": "Asia/Shanghai"},
    "tags": ["developer", "premium"],
    "trust_score": 4.5
}'),
(2, '{
    "theme": "light",
    "notifications": {"email": false, "sms": true, "push": false},
    "preferences": {"language": "en", "timezone": "America/New_York"},
    "tags": ["basic"]
}');

-- 创建 GIN 索引
CREATE INDEX idx_config_gin ON user_configs USING GIN (config);
```

## 查询示例

```sql
-- 1. 查询所有使用深色主题的用户
SELECT user_id, config ->> 'theme' AS theme
FROM user_configs
WHERE config @> '{"theme": "dark"}';

-- 2. 查询开启了邮件通知的用户
SELECT user_id FROM user_configs
WHERE config @> '{"notifications": {"email": true}}';

-- 3. 查询有 trust_score 字段的用户
SELECT user_id FROM user_configs WHERE config ? 'trust_score';

-- 4. 查询语言为中文的高级用户 (tags 包含 "premium")
SELECT user_id FROM user_configs
WHERE config @> '{"preferences": {"language": "zh-CN"}}'
  AND config @> '{"tags": ["premium"]}';

-- 5. 更新嵌套字段（开启 SMS 通知）
UPDATE user_configs SET config = JSONB_SET(
    config, '{notifications, sms}', 'true'::JSONB
) WHERE user_id = 1;

-- 6. 追加标签
UPDATE user_configs SET config = config || '{"tags": ["vip"]}'
WHERE user_id = 1;

-- 7. 展开 JSONB 查看所有键值对
SELECT key, value FROM user_configs c,
JSONB_EACH(c.config) WHERE user_id = 1;

-- 8. 聚合用户配置为 JSONB 数组
SELECT JSONB_AGG(config) AS all_configs FROM user_configs;
```
