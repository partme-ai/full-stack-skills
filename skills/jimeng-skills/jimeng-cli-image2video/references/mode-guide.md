# Mode Selection Guide — I2V 子命令选择指南

> 根据输入类型和用户意图选择正确的子命令。

---

## 决策树

```
用户有多少参考素材？
├── 1张图片
│   └── dreamina image2video           # 单图生视频
├── 2张图片
│   ├── 是首尾帧关系（从A变到B）？
│   │   └── dreamina frames2video      # 首尾帧
│   └── 是连续故事帧？
│       └── dreamina multiframe2video  # 多帧故事
├── 3-20张图片（故事板序列）
│   └── dreamina multiframe2video      # 多帧故事
└── 图片 + 视频/音频混合
    └── dreamina multimodal2video      # 全能参考
```

## 模式能力对比

| 能力 | image2video | frames2video | multiframe2video | multimodal2video |
|------|-----------|-------------|-----------------|-----------------|
| 输入类型 | 1图 | 2图 | 2-20图 | 图+视频+音频 |
| 运动控制 | 提示词 | 提示词 | 提示词+帧 | 提示词+视频参考 |
| 过渡控制 | — | — | transition-prompt | — |
| 音频驱动 | — | — | — | ✅ |
| 视频参考 | — | — | — | ✅ |
| 复杂度 | 低 | 中 | 高 | 最高 |
| 控制精度 | 中 | 高 | 最高 | 最高 |
| 适用 | 微动化 | 形态变化 | 叙事 | 精确合成 |

## 场景-模式对照

| 用户需求 | 推荐模式 | 理由 |
|---------|---------|------|
| "让这张照片里的人眨眼微笑" | image2video | 单图微动 |
| "让这张风景照的水流动起来" | image2video | 单图元素微动 |
| "从花苞变成盛开的花" | frames2video | A→B形态变化 |
| "从夏天变成秋天" | frames2video | 季节过渡 |
| "用5张图讲一个小故事" | multiframe2video | 叙事序列 |
| "产品使用步骤演示" | multiframe2video | 步骤序列 |
| "把这个人物放到那个场景里动起来" | multimodal2video | 人物+场景分离 |
| "让这张照片里的人跟着音乐节奏说话" | multimodal2video | 音频驱动 |

## 常见误路由

| 错误 | 后果 | 正确做法 |
|------|------|---------|
| 2张首尾帧用 image2video | 只能上传1张 | 用 frames2video --first --last |
| 2张序列用 frames2video | 强制首尾逻辑，中间不可控 | 用 multiframe2video |
| 多素材用 multiframe2video | 不支持视频/音频 | 用 multimodal2video |
