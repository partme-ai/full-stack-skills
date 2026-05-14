# processon-diagram-generator

用 ProcessOn 生成专业、可继续编辑的图形，支持自然语言、代码上下文。

## 安装与首要配置

### 1. 安装技能

**通过 full-stack-skills（推荐）：**

```bash
/plugin install document-skills@full-stack-skills
```

或单独安装本技能：

```bash
npx skills add https://github.com/partme-ai/full-stack-skills.git --skill processon-diagram-generator
```

**通过 ProcessOn 官方仓库：**

```bash
npx skills add https://github.com/processonai/processon-skills.git --skill processon-diagram-generator
```
#### 更新技能
```bash
npx skills add https://github.com/processonai/processon-skills.git --skill processon-diagram-generator --force -g -y
```

### 2. 获取 API Key (核心步骤)
本技能依赖 ProcessOn 智能绘图接口。请务必访问以下地址获取你的 `PROCESSON_API_KEY`：

**👉 [获取 API Key/Token](https://smart.processon.com/user)**

### 3. 设置环境变量
将获取到的 Key 设置为系统环境变量：

> **重要提示**：请务必在**当前运行 Agent 的终端**中设置环境变量。如果你使用的是 IDE 内置终端，设置后可能需要重启 IDE 或重启 Agent 宿主进程以使配置生效。

**macOS / Linux:**
```bash
export PROCESSON_API_KEY="你的-API-Key"
```

**Windows (PowerShell):**
```powershell
$env:PROCESSON_API_KEY="你的-API-Key"
```

**Windows (CMD):**
```cmd
set PROCESSON_API_KEY=你的-API-Key
```

## 支持的图形类型

- 流程图
- 业务流程图
- 泳道图
- 流程地图
- 标准流程图
- 时序图
- 软件架构图
- 系统架构图
- 云架构图
- ER 图
- 组织结构图
- 时间轴
- 信息图
- 金字塔图


## 提示词示例

```text
生成一个登录注册流程图，要求布局清晰，适合产品和研发沟通
```

```text
生成一个订单创建、支付、库存扣减的时序图
```

```text
分析这个项目的模块关系并生成系统架构图，不要画目录树
```

```text
把这张手绘草图重绘成流程图
```

## 输出

- 图片链接。
- 图形的dsl

dsl编辑链接：

```text
https://smart.processon.com/editor
```

## 本地开发

如果你想在本地迭代这个 skill，而不是从 GitHub 安装，可以把 skill 目录放到本地 skills 目录，例如：

```text
~/.agents/skills/processon-diagram-generator
```
