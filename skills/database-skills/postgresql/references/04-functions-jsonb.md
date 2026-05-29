# JSONB 函数与操作详解

## 访问操作符

```sql
-- -> 返回 JSONB, ->> 返回 TEXT
SELECT
    config -> 'theme' AS theme_jsonb,              -- "dark"
    config ->> 'theme' AS theme_text,              -- dark
    config -> 'notifications' -> 'email' AS email_jsonb,
    config #>> '{preferences, language}' AS lang

FROM user_configs WHERE user_id = 1;

-- #> / #>> 路径访问
SELECT config #> '{preferences, timezone}' AS tz,
       config #>> '{notifications, push}' AS push
FROM user_configs WHERE user_id = 1;
```

## 包含与存在操作

```sql
-- @> — 包含（业务场景：查询包含特定配置的用户）
SELECT user_id, config FROM user_configs
WHERE config @> '{"notifications": {"email": true}}';

-- ? — 是否存在键
SELECT user_id FROM user_configs WHERE config ? 'trust_score';

-- ?| — 存在任意键
SELECT user_id FROM user_configs WHERE config ?| ARRAY['trust_score', 'vip_level'];

-- ?& — 包含所有键
SELECT user_id FROM user_configs WHERE config ?& ARRAY['theme', 'notifications'];
```

## 修改函数

```sql
-- || — JSONB 合并
UPDATE user_configs SET config = config || '{"vip_level": 2}' WHERE user_id = 1;

-- JSONB_SET — 设置路径值
UPDATE user_configs SET config = JSONB_SET(config, '{notifications, email}', 'false'::JSONB)
WHERE user_id = 1;

-- JSONB_INSERT — 插入不覆盖 (PG 9.6+)
SELECT JSONB_INSERT('{"a":1,"b":2}'::JSONB, '{c}', '3'::JSONB);

-- JSONB_STRIP_NULLS — 移除 null
SELECT JSONB_STRIP_NULLS('{"a":1,"b":null}'::JSONB);  -- {"a": 1}
```

## 构建函数

```sql
-- JSONB_BUILD_OBJECT / JSONB_BUILD_ARRAY
SELECT JSONB_BUILD_OBJECT(
    'id', 101, 'name', 'Alice',
    'roles', JSONB_BUILD_ARRAY('admin', 'editor'),
    'meta', JSONB_BUILD_OBJECT('last_login', NOW())
);
```

## 展开函数

```sql
-- JSONB_EACH — 展开为 (key, value) 行集
SELECT * FROM JSONB_EACH((SELECT config FROM user_configs WHERE user_id = 1));

-- JSONB_EACH_TEXT — 展开为 (key, text_value)
SELECT * FROM JSONB_EACH_TEXT((SELECT config FROM user_configs WHERE user_id = 1));

-- JSONB_OBJECT_KEYS — 仅返回键
SELECT * FROM JSONB_OBJECT_KEYS((SELECT config FROM user_configs WHERE user_id = 1));

-- JSONB_EXTRACT_PATH — 提取路径
SELECT JSONB_EXTRACT_PATH(config, 'preferences', 'language') FROM user_configs;
```

## 类型检查与格式化

```sql
-- JSONB_TYPEOF (PG 14+)
SELECT JSONB_TYPEOF(config -> 'theme'),   -- string
       JSONB_TYPEOF(config -> 'tags'),     -- array
       JSONB_TYPEOF(config -> 'trust_score') -- number
FROM user_configs WHERE user_id = 1;

-- JSONB_PRETTY (PG 14+)
SELECT JSONB_PRETTY(config) FROM user_configs WHERE user_id = 1;
```

## GIN 索引

```sql
-- 标准 GIN
CREATE INDEX idx_config_gin ON user_configs USING GIN (config);

-- jsonb_path_ops（更小更快，不支持 ? 操作符）
CREATE INDEX idx_config_path ON user_configs USING GIN (config jsonb_path_ops);
```

## 完整示例表

```sql
CREATE TABLE user_configs (
    id      BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    config  JSONB NOT NULL DEFAULT '{}'
);

INSERT INTO user_configs (user_id, config) VALUES
(1, '{"theme":"dark","notifications":{"email":true},"preferences":{"language":"zh-CN","timezone":"Asia/Shanghai"},"tags":["developer","premium"],"trust_score":4.5}'),
(2, '{"theme":"light","notifications":{"email":false},"preferences":{"language":"en","timezone":"America/New_York"},"tags":["basic"]}');
```
