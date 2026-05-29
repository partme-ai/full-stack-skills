# 分词器 (Analyzer)

分词器将文本拆分为词项 (Token)，用于建立倒排索引和搜索。

## Analyzer 组成

```
Analyzer = Char Filter(s) + Tokenizer + Token Filter(s)
           (字符过滤)      (分词器)     (词项过滤)

输入: "I &lt;3 Elasticsearch!"
    ↓
char_filter: HTML 解码 → "I <3 Elasticsearch!"
    ↓
tokenizer: 按空格/标点拆分 → ["I", "<3", "Elasticsearch"]
    ↓
token_filter: 小写化 → ["i", "<3", "elasticsearch"]
    ↓
输出: ["i", "<3", "elasticsearch"] (存入倒排索引)
```

## 测试分词器

```bash
# 测试分析器效果
POST /_analyze
{
  "analyzer": "standard",
  "text": "I love Elasticsearch 搜索引擎"
}

# 指定字段测试 (使用字段配置的分析器)
POST /products/_analyze
{
  "field": "title",
  "text": "Apple MacBook Pro 16英寸"
}
```

## 内置分词器

| 分词器 | 说明 | 示例: "I love ES" |
|--------|------|------------------|
| `standard` | Unicode 分词, 小写化 (默认) | ["i", "love", "es"] |
| `simple` | 非字母分割, 小写化 | ["i", "love", "es"] |
| `whitespace` | 空格分割 (不小写) | ["I", "love", "ES"] |
| `keyword` | 不分词, 整个字符串输出 | ["I love ES"] |
| `pattern` | 正则分割 | 取决于 pattern |
| `stop` | 类似 simple + 去停用词 | ["love", "es"] |
| `fingerprint` | 排序 + 去重 | ["es", "i", "love"] |

## IK 分词器 (中文)

```bash
# 安装 (需重启 ES)
./bin/elasticsearch-plugin install \
  https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v8.12.0/elasticsearch-analysis-ik-8.12.0.zip

# ik_smart (粗粒度)
POST /_analyze { "analyzer": "ik_smart", "text": "中华人民共和国国歌" }
# → ["中华人民共和国", "国歌"]

# ik_max_word (细粒度, 穷尽所有可能)
POST /_analyze { "analyzer": "ik_max_word", "text": "中华人民共和国国歌" }
# → ["中华人民共和国", "中华人民", "中华", "华人", "人民共和国", "人民", "共和国", "共和", "国歌"]
```

| 场景 | 推荐 | 理由 |
|------|------|------|
| 索引 (建倒排索引) | `ik_max_word` | 细粒度, 覆盖更多可能性 |
| 搜索 (用户输入) | `ik_smart` | 粗粒度, 提高搜索精度 |

## 拼音分词器

```bash
./bin/elasticsearch-plugin install \
  https://github.com/medcl/elasticsearch-analysis-pinyin/releases/download/v8.12.0/elasticsearch-analysis-pinyin-8.12.0.zip

# 测试
POST /_analyze { "analyzer": "pinyin", "text": "王大力" }
# → ["wang", "da", "li", "wangda", "dali", "wangdali", "wdl"]

# 拼音字段配置
PUT /products
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "ik_max_word",
        "fields": {
          "pinyin": {
            "type": "text",
            "analyzer": "pinyin",
            "search_analyzer": "pinyin"
          }
        }
      }
    }
  }
}
# 搜索 "wdali" → 匹配 "王大力"
```

## 自定义分析器

```json
PUT /my_index
{
  "settings": {
    "analysis": {
      "char_filter": {
        "html_strip": { "type": "html_strip" },
        "my_mapping": {
          "type": "mapping",
          "mappings": ["& => and", "| => or"]
        }
      },
      "tokenizer": {
        "my_standard": { "type": "standard", "max_token_length": 100 }
      },
      "filter": {
        "my_stop": {
          "type": "stop",
          "stopwords": ["a", "an", "the", "is"]
        },
        "my_synonym": {
          "type": "synonym",
          "synonyms": [
            "笔记本, 笔记本电脑, laptop",
            "手机, 移动电话, smartphone"
          ]
        }
      },
      "analyzer": {
        "my_custom_analyzer": {
          "type": "custom",
          "char_filter": ["html_strip", "my_mapping"],
          "tokenizer": "my_standard",
          "filter": ["lowercase", "my_stop", "my_synonym", "asciifolding"]
        }
      }
    }
  }
}
```

## 自动补全 (Edge Ngram)

```json
PUT /autocomplete_index
{
  "settings": {
    "analysis": {
      "filter": {
        "autocomplete_filter": {
          "type": "edge_ngram",
          "min_gram": 1,
          "max_gram": 20
        }
      },
      "analyzer": {
        "autocomplete": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "autocomplete_filter"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "autocomplete",
        "search_analyzer": "standard"
      }
    }
  }
}
```

## 同义词注意事项

- **单向同义词**: `"laptop => 笔记本"` (搜索 laptop 映射到笔记本)
- **双向同义词**: `"laptop, 笔记本"` (互相等价)
- **最佳实践**: 索引时不用同义词（保持原始词），搜索时用 `search_analyzer`
