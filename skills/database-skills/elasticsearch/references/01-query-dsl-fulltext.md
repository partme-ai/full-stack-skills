# 全文查询 (Full Text Queries)

全文查询会对查询文本进行分词，然后搜索倒排索引。这些查询会计算相关性分数 (`_score`)。

## match — 标准全文匹配

```bash
# 基本 match (默认 OR 逻辑)
GET /products/_search
{
  "query": {
    "match": {
      "title": "apple macbook"
    }
  }
}

# AND 逻辑 (必须匹配所有词项)
GET /products/_search
{
  "query": {
    "match": {
      "title": {
        "query": "apple macbook",
        "operator": "and"
      }
    }
  }
}

# minimum_should_match (至少匹配 75% 词项)
GET /products/_search
{
  "query": {
    "match": {
      "title": {
        "query": "apple macbook pro",
        "minimum_should_match": "75%"
      }
    }
  }
}
```

**业务场景**：商品搜索、文章搜索、文档搜索。用户输入关键词时自动分词匹配。

## match_phrase — 短语匹配

```bash
# 精确短语匹配 (顺序必须一致)
GET /products/_search
{
  "query": {
    "match_phrase": {
      "title": "macbook pro"
    }
  }
}

# 带 slop 的短语匹配 (允许词项间插入 slop 个词)
GET /products/_search
{
  "query": {
    "match_phrase": {
      "title": {
        "query": "macbook pro",
        "slop": 1
      }
    }
  }
}
```

**业务场景**：搜索"红米手机"不希望匹配"红色小米手机"；搜索完整书名/产品名。

## multi_match — 多字段匹配

```bash
# 同时在 title 和 description 中搜索
GET /products/_search
{
  "query": {
    "multi_match": {
      "query": "轻薄笔记本",
      "fields": ["title", "description"]
    }
  }
}

# 带权重 (title 字段权重 2 倍)
GET /products/_search
{
  "query": {
    "multi_match": {
      "query": "轻薄笔记本",
      "fields": ["title^2", "description", "tags^0.5"]
    }
  }
}

# type 说明:
# - best_fields (默认): 取最佳匹配字段分数
# - most_fields: 合并所有匹配字段分数
# - cross_fields: 将词项拆分到多字段 (适合姓名搜索)
GET /products/_search
{
  "query": {
    "multi_match": {
      "query": "Will Smith",
      "fields": ["first_name", "last_name"],
      "type": "cross_fields"
    }
  }
}
```

**业务场景**：搜索框同时匹配标题、描述、标签等字段；人名搜索。

## query_string — 完整查询语法

```bash
# 支持 AND/OR/NOT, 通配符, 正则等
GET /products/_search
{
  "query": {
    "query_string": {
      "query": "title:(apple AND macbook) AND price:[10000 TO 20000]",
      "default_operator": "and"
    }
  }
}

# 支持短语和多字段
GET /products/_search
{
  "query": {
    "query_string": {
      "query": "\"macbook pro\" OR \"iphone\"",
      "fields": ["title^2", "description"]
    }
  }
}
```

**注意**：query_string 解析语法错误会抛出异常，生产环境推荐用 `simple_query_string`。

## simple_query_string — 安全版查询语法

```bash
GET /products/_search
{
  "query": {
    "simple_query_string": {
      "query": "\"macbook pro\" +apple -samsung",
      "fields": ["title", "description"],
      "default_operator": "or"
    }
  }
}
```

**支持语法**：`+` (AND), `|` (OR), `-` (NOT), `"` (短语), `*` (前缀)。语法错误不会抛异常。
