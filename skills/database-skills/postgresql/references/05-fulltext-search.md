# 全文搜索详解

## 基础概念

PostgreSQL 全文搜索基于 **tsvector** (文本搜索向量) 和 **tsquery** (文本搜索查询)，配合 GIN 索引实现高效搜索。

## 建表与索引

```sql
CREATE TABLE documents (
    id          SERIAL PRIMARY KEY,
    title       TEXT NOT NULL,
    body        TEXT NOT NULL,
    body_tsv    TSVECTOR GENERATED ALWAYS AS (to_tsvector('english', body)) STORED
);

CREATE INDEX idx_documents_body_tsv ON documents USING GIN (body_tsv);

INSERT INTO documents (title, body) VALUES
    ('PostgreSQL Full Text Search',
     'PostgreSQL provides full-text search capabilities out of the box.'),
    ('Indexing Strategies',
     'Proper indexing is crucial for database performance. GIN indexes are optimized for full-text search.'),
    ('Database Performance Tuning',
     'Performance tuning involves many aspects including query optimization, indexing strategy, and hardware configuration.');
```

## 核心函数

```sql
-- to_tsvector — 文本转搜索向量（停用词被移除, 动词被词根化）
SELECT to_tsvector('english', 'The quick brown fox jumps over the lazy dog');
-- 'brown':3 'dog':9 'fox':4 'jump':5 'lazi':8 'quick':2

-- to_tsquery — 文本转搜索查询
SELECT to_tsquery('english', 'search & indexing');
-- 'search' & 'index'

-- plainto_tsquery — 简单转换（空格分隔的单词自动加 &）
SELECT plainto_tsquery('english', 'full text search');
-- 'full' & 'text' & 'search'
```

## 匹配查询

```sql
-- @@ — 全文搜索匹配操作符
SELECT id, title FROM documents
WHERE body_tsv @@ to_tsquery('english', 'search & index');

-- plainto_tsquery 简化写法
SELECT id, title FROM documents
WHERE body_tsv @@ plainto_tsquery('english', 'full text search');

-- 直接对原始列搜索（不依赖 tsvector 列）
SELECT id, title FROM documents
WHERE to_tsvector('english', body) @@ to_tsquery('english', 'search');
```

## 排序与高亮

```sql
-- ts_rank / ts_rank_cd — 相关性排序
SELECT id, title, ts_rank(body_tsv, query) AS rank
FROM documents, to_tsquery('english', 'search & indexing') AS query
WHERE body_tsv @@ query ORDER BY rank DESC;

-- ts_headline — 高亮摘要
SELECT id, ts_headline('english', body, query,
    'StartSel=<mark>, StopSel=</mark>, MaxWords=30, MinWords=10') AS highlighted
FROM documents, plainto_tsquery('english', 'full text search') AS query
WHERE body_tsv @@ query;
```

## 短语搜索

```sql
-- <-> : 相邻单词
SELECT * FROM documents
WHERE body_tsv @@ to_tsquery('english', 'full <-> text <-> search');

-- <N> : 相隔最多 N 个词
SELECT * FROM documents
WHERE body_tsv @@ to_tsquery('english', 'performance <2> tuning');
-- 匹配 "performance tuning" 或 "performance and tuning"
```

## 中文全文搜索

```sql
-- 需要 zhparser 或 jieba 扩展
-- CREATE EXTENSION zhparser;
-- CREATE TEXT SEARCH CONFIGURATION chinese (PARSER = zhparser);
-- ALTER TEXT SEARCH CONFIGURATION chinese ADD MAPPING FOR n,v,a,i,e,l WITH simple;
-- SELECT to_tsvector('chinese', '数据库性能优化技巧');
```

## 多语言与自定义配置

```sql
-- simple: 不做词干分析
SELECT to_tsvector('simple', 'running runs ran');  -- 'running':1 'runs':2 'ran':3

-- english: 词干分析
SELECT to_tsvector('english', 'running runs ran');  -- 'run':1,2,3

-- 创建自定义字典
CREATE TEXT SEARCH DICTIONARY my_dict (TEMPLATE = pg_catalog.simple, ...);
```
