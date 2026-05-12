# Parameter Reference — dreamina image2image 完整参数手册

> `dreamina image2image` 命令的完整参数参考。运行前先执行 `dreamina image2image -h` 确认最新参数。

---

## 必需参数

| 参数 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `--images` | path(s) | 1-10张本地图片，逗号分隔 | `--images ./photo.png` 或 `--images ./a.png,./b.png` |
| `--prompt` | string | 编辑提示词（Keep/Change风格） | `--prompt="保持人物不变，将背景替换为海滩"` |

## 可选参数

### --ratio（宽高比）

同 `dreamina text2image`，8种选项：
`21:9` · `16:9` · `3:2` · `4:3` · `1:1` · `3:4` · `2:3` · `9:16`

默认值：`1:1`

### --model_version（模型版本）

| 值 | 说明 |
|----|------|
| `5.0` | 最新旗舰，默认推荐 |
| `4.6` | 人像/面部/产品编辑 |
| `4.5` | 风景/艺术风格转换 |
| `4.1` | 通用稳定 |
| `4.0` | I2I最低版本要求 |

> **I2I 限制**: 仅支持 4.0 及以上。不支持 3.0/3.1。

### --resolution_type（分辨率）

| 值 | 说明 |
|----|------|
| `2k` | 标准分辨率，默认 |
| `4k` | 高分辨率，细节更丰富 |

> **I2I 限制**: 仅支持 2k 和 4k。不支持 1k。

### --poll（轮询秒数）

| 值 | 行为 |
|----|------|
| `0` | 异步模式 |
| `30` | **推荐**，适合大多数I2I任务 |
| `60` | 适合4K高分辨率编辑 |

Poll 每秒轮询1次。超时返回 "querying" 中间结果（非失败）。

---

## 完整命令示例

### 风格迁移
```bash
dreamina image2image \
  --images ./photo.png \
  --prompt="保持人物面部特征和构图，转换为水墨画风格，黑白灰墨色，大面积留白，宣纸质感" \
  --model_version=5.0 \
  --resolution_type=4k \
  --poll=30
```

### 背景替换
```bash
dreamina image2image \
  --images ./person.png \
  --prompt="保持人物、姿势和服装完全不变。将替换为东京霓虹灯夜景。调整人物边缘光匹配霓虹色温。在脚下添加自然阴影。" \
  --ratio=3:4 \
  --poll=30
```

### 多图参考合成
```bash
dreamina image2image \
  --images ./subject.png,./style.png,./background.png \
  --prompt="参考第一张的人物特征，应用第二张的艺术风格，配上第三张的背景环境。所有元素统一光源方向。全局色彩协调。" \
  --poll=30
```

### 异步提交
```bash
dreamina image2image --images ./input.png --prompt="..." --poll=0
# 保存 submit_id
```

---

## 参数映射速查

| 提示词输出 | CLI 参数 | 映射规则 |
|-----------|---------|---------|
| 建议模型 4.5+ | `--model_version=5.0` | 向上取整到最新稳定版 |
| 4K画质 | `--resolution_type=4k` | 直接映射 |
| 比例 3:4 | `--ratio=3:4` | 直接映射 |
| (未指定) | 省略参数 | 使用CLI默认值 |

---

## 图片文件要求

- **格式**: PNG, JPG, JPEG, WEBP
- **数量**: 1-10 张
- **路径**: 必须为本地绝对路径或相对路径（不支持URL）
- **多图语法**: `--images ./a.png,./b.png`（逗号分隔）
- **验证**: 提交前用 `ls -la <path>` 确认文件存在且可读
