# Writing Rules

### Rule 1: Be specific, not generic

Replace vague adjectives with concrete, visual details:
- ✗ "好看的夕阳" → ✓ "夕阳透过梧桐树叶洒下斑驳光影，天空从橙渐变到深紫"
- ✗ "美丽的风景" → ✓ "晨雾中的梯田，水面如镜反射朝霞，远山层叠如黛"

### Rule 2: Use positive descriptions

即梦 cannot process negations ("不要红色", "no red"). Always describe what you WANT:
- ✗ "不要现代建筑" → ✓ "传统木质结构建筑，青砖灰瓦"
- ✗ "no people in the scene" → ✓ "空旷无人的街道，静谧安详"

### Rule 3: Order by importance

Place the most important visual elements first. The model weights earlier tokens more heavily:
- Portrait: subject → clothing → expression → scene → lighting → style → quality
- Landscape: environment → time/weather → color → style → composition → quality
- Product: object → material/texture → placement → background → lighting → style → quality

### Rule 4: Match length and style to model version

| 版本 | 提示词风格 | 长度建议 | 特点 |
|------|-----------|----------|------|
| **2.1** | 结构化分类标签 | 40-80字 | 使用"材料技法/色彩/镜头语言"等分类关键词；推荐国风词 |
| **3.0** | 简洁精准 | 40-80字 | 文字用 `"引号"` 包裹；专业词汇用英文/原文；写清楚用途类型（如`PPT背景图`、`广告海报设计`） |
| **3.1** | 电影感故事性 | 60-120字 | 善用电影类型词（爱情片/史诗片/公路片）；风格精准度高 |
| **4.0+** | 细节丰富 | 80-150字 | 可写复杂多元素描述；支持自然语言编辑指令 |
| **4.5+** | 详细丰富 | 100-200字 | 推理能力更强，支持复杂逻辑关系；人像类效果最佳 |
| **5.0** | 联网增强 | 80-150字 | 可包含品牌/名人/时事关键词触发联网检索；支持2K/4K高清 |

通用原则：当不确定版本时，提供简洁和详细两个版本。

### Rule 5: Choose aspect ratio for the content

- **1:1** — product shots, profile pictures, square compositions
- **3:4 or 9:16** — full-body portraits, fashion, vertical scenes
- **16:9 or 21:9** — landscapes, cinematic scenes, wide compositions
- **4:3** — general purpose, balanced compositions

### Rule 6: Anchor the style

Style keywords in the latter half of the prompt strongly influence the output aesthetic. Place the primary style descriptor just before quality words:
```
[detailed subject + scene description] + [摄影风格/艺术风格] + [画质词]
```

### Rule 7: Text content in quotation marks (3.0 model tip)

For prompts that include text/words in the image, wrap the desired text in `"引号"` to improve accuracy:
```
文字为"呼伦贝尔肉业集团春季推广"，位于左下角
```

### Rule 8: Specify purpose and type (3.0 model tip)

Writing the image's purpose and type helps 3.0 model produce more targeted results:
- 用途：PPT封面背景图、背景素材图
- 类型：广告海报设计、纪实摄影、电商主图

### Rule 9: Short prompts can be effective (3.0 model tip)

Short, precise natural language can outperform long AI-generated prompts. Use:
- **Natural sentences** for scene content: "一个女孩在森林里漫步，阳光透过树叶洒下"
- **Short tags** for aesthetics: "冷色调，胶片质感，氛围感，极简"
- Professional vocabulary works best in original language (English for technical, 中文 for Chinese aesthetics)
