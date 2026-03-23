# Optimized Prompt Output Examples (中英文示例)

Based on the **「优化后的提示词」** (optimized prompt) structure from the blog **《Trae+Stitch MCP+Skills：我的AI编程新范式》**. Use these as reference when assembling Stitch prompts so the model receives a precise construction blueprint (project overview + design system + page structure and function).

---

## 一、中文示例：配料表翻译官小程序

（来源：博客原文优化后的提示词）

```text
# 优化后的配料表翻译官小程序提示词

## 项目概述
一款专为中文用户设计的AI食品配料表分析工具，通过图像识别和成分解析，将专业化学术语转化为通俗易懂的语言，帮助用户轻松了解食品的真实营养成分和健康影响。整体风格采用现代简约设计，注重易用性和信息可读性，全中文界面，符合国内用户使用习惯。

## 设计系统（必填）
- **平台**: 移动端小程序，优先适配主流移动设备
- **主题**: 明亮清新，专业可信，带有医疗健康领域的亲和力
- **色彩方案**:
  - 主色调：健康蓝 (#165DFF) - 用于按钮、导航和重点强调
  - 辅助色：活力绿 (#36D399) - 用于健康评分和积极提示
  - 警示色：警告橙 (#FF9F43) - 用于潜在风险提示
  - 中性色：
    - 背景：纯净白 (#FFFFFF)
    - 文本：深邃黑 (#1D2129)
    - 辅助文本：中性灰 (#86909C)
    - 分割线：浅灰 (#F2F3F5)
- **排版**:
  - 标题：20px 无衬线字体 Bold
  - 正文：16px 无衬线字体 Regular
  - 辅助文字：14px 无衬线字体 Light
- **组件风格**:
  - 按钮：圆角8px，阴影柔和，交互反馈清晰
  - 卡片：圆角12px，轻微阴影，营造层次感
  - 图标：线性风格，简洁明了

## 页面结构与功能

### 1. 首页（拍摄/上传页面）
**核心功能**: 应用入口，引导用户开始使用
- **顶部导航**: 品牌logo + 帮助入口
- **主视觉区**: 醒目标题"配料表翻译官" + 副标题"一键读懂食品成分"
- **功能区**:
  - 主要操作按钮："拍照识别"（大尺寸，主色调填充）
  - 次要操作按钮："从相册选择"（边框样式，主色调描边）
  - 使用引导：简洁图文说明，展示操作流程
- **底部提示**: 隐私声明和使用条款链接

### 2. 识别结果页面
**核心功能**: 展示识别的原始文本和初步分析结果
- **顶部导航**: 返回按钮 + 标题"识别结果"
- **原始文本区**:
  - 标题："识别的配料表文本"
  - 内容：可滚动文本区域，展示OCR识别的原始配料表
- **初步分析区**:
  - 标题："初步分析"
  - 内容：识别到的成分数量、主要成分概览
- **操作区**:
  - 按钮1："重新识别"（边框样式）
  - 按钮2："开始分析"（主色调填充，大尺寸）

### 3. 分析结果页面
**核心功能**: 展示详细的成分分析和健康评估
- **顶部导航**: 返回按钮 + 分享按钮 + 标题"分析结果"
- **健康评分区**:
  - 可视化评分：圆形进度条展示健康评分（0-100分）
  - 评分说明：文字解释评分依据和含义
- **成分翻译区**:
  - 标题："成分通俗翻译"
  - 列表展示：专业术语 → 通俗解释（如："山梨酸钾" → "常见防腐剂，适量使用安全"）
- **营养成分表**:
  - 标准表格格式：展示能量、蛋白质、脂肪、碳水化合物等核心营养数据
- **健康建议区**:
  - 个性化建议：根据成分分析给出针对性健康提示
  - 风险提示：高亮显示需要注意的成分

### 4. 结果分享页面
**核心功能**: 提供多种分享方式，支持自定义分享文案
- **顶部导航**: 返回按钮 + 标题"分享结果"
- **分享预览区**:
  - 生成的分享图片预览（包含健康评分、主要成分和二维码）
- **自定义文案区**:
  - 预设文案："这款食品的健康评分是XX分，主要成分有XX，XX，XX。"
  - 编辑功能：允许用户修改分享文案
- **分享方式区**:
  - 常用分享渠道：好友、动态、保存图片
  - 其他选项：复制链接、更多分享方式
```

---

## 二、English Example: Ingredient Label Translator App

(Same product concept and structure, in English for Stitch / international use.)

```text
# Optimized Prompt: Ingredient Label Translator

## Project Overview
An AI-powered ingredient list analysis tool for everyday users. It turns chemical terms on food labels into plain language via image recognition and composition parsing, so users can easily understand real nutrition and health impact. Modern minimal design, emphasis on ease of use and information readability, full localized interface aligned with target users.

## Design System (Required)
- **Platform**: Mobile miniapp / app, prioritize mainstream mobile devices
- **Theme**: Bright and fresh, professional and trustworthy, with a health/wellness-friendly tone
- **Color scheme**:
  - Primary: Health blue (#165DFF) — buttons, navigation, key emphasis
  - Secondary: Vital green (#36D399) — health score and positive cues
  - Warning: Caution orange (#FF9F43) — potential risk cues
  - Neutrals:
    - Background: Pure white (#FFFFFF)
    - Text: Deep black (#1D2129)
    - Secondary text: Neutral grey (#86909C)
    - Divider: Light grey (#F2F3F5)
- **Typography**:
  - Title: 20px sans-serif Bold
  - Body: 16px sans-serif Regular
  - Auxiliary: 14px sans-serif Light
- **Component style**:
  - Buttons: 8px radius, soft shadow, clear interaction feedback
  - Cards: 12px radius, light shadow, clear hierarchy
  - Icons: Linear, minimal

## Page Structure and Function

### 1. Home (Scan / Upload)
**Core function**: App entry, guide user to start
- **Top nav**: Brand logo + Help entry
- **Hero**: Headline "Ingredient Translator" + subhead "Understand food labels at a glance"
- **Function area**:
  - Primary CTA: "Scan label" (large, primary fill)
  - Secondary: "Choose from gallery" (outline, primary border)
  - Short usage copy with simple illustration of flow
- **Footer**: Privacy and terms links

### 2. Recognition Result
**Core function**: Show raw OCR text and preliminary analysis
- **Top nav**: Back + title "Recognition Result"
- **Raw text area**:
  - Label: "Recognized ingredient text"
  - Content: Scrollable text block with OCR output
- **Preliminary analysis**:
  - Label: "Preliminary analysis"
  - Content: Ingredient count, main ingredients overview
- **Actions**:
  - Button 1: "Scan again" (outline)
  - Button 2: "Analyze" (primary fill, large)

### 3. Analysis Result
**Core function**: Detailed ingredient analysis and health assessment
- **Top nav**: Back + Share + title "Analysis Result"
- **Health score**:
  - Circular progress (0–100) for health score
  - Short copy explaining score and meaning
- **Ingredient translation**:
  - Label: "Plain-language ingredients"
  - List: term → explanation (e.g. "Potassium sorbate" → "Common preservative, safe in normal amounts")
- **Nutrition table**:
  - Standard table: energy, protein, fat, carbs, etc.
- **Health tips**:
  - Personalized tips from analysis
  - Risk callouts for ingredients to watch

### 4. Share Result
**Core function**: Multiple share options and editable share copy
- **Top nav**: Back + title "Share Result"
- **Share preview**:
  - Preview of share image (health score, main ingredients, QR if needed)
- **Custom copy**:
  - Default: "This product's health score is XX. Main ingredients: XX, XX, XX."
  - Editable by user
- **Share options**:
  - Primary: Share to contacts, feed, Save image
  - Other: Copy link, More
```

---

## Structure Checklist (通用结构检查)

When producing an optimized prompt, ensure:

| Section | 中文 | English |
|--------|------|--------|
| 项目概述 / Project overview | 一段话：是什么、给谁、风格、关键属性 | One paragraph: what, who, style, key attributes |
| 设计系统（必填）/ Design system | 平台、主题、色彩(#hex)、排版(px+字体+字重)、组件风格 | Platform, theme, colors (#hex), typography (px+font+weight), component style |
| 页面结构与功能 / Page structure | 每页：核心功能 + 区域（顶部/主视觉/功能区/操作区/底部） + 具体元素 | Per page: core function + areas + concrete elements |

Reference: [SKILL.md](../SKILL.md) → **Prompt Quality Standard: Optimized Prompt Structure**.
