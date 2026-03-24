# Agent Skills 入门指南：从零到一的架构师视角

> **作者视角**：资深架构师  
> **目标读者**：希望掌握 Agent Skills 的开发者、技术负责人  
> **文档定位**：入门级教程，但包含架构设计的深度思考

---

## 目录

1. [什么是 Agent Skills？](#什么是-agent-skills)
2. [为什么需要 Agent Skills？](#为什么需要-agent-skills)
3. [核心架构：渐进式披露机制](#核心架构渐进式披露机制)
4. [技能结构：从文件到能力](#技能结构从文件到能力)
5. [创建你的第一个技能](#创建你的第一个技能)
6. [架构师的最佳实践](#架构师的最佳实践)
7. [常见问题与解决方案](#常见问题与解决方案)
8. [下一步学习](#下一步学习)

---

## 什么是 Agent Skills？

### 从"工具调用"到"能力工程"

在传统的 AI 应用开发中，我们通常通过以下方式扩展 AI 的能力：

- **System Prompt（系统提示词）**：在对话开始时注入长段的指令，告诉 AI 如何工作
- **Tool Calling（工具调用）**：让 AI 调用外部 API 或执行脚本
- **Few-Shot Examples（少样本示例）**：在提示词中提供示例，引导 AI 的行为

这些方式虽然有效，但存在明显的问题：

1. **上下文膨胀**：System Prompt 越来越长，消耗大量 Token
2. **碎片化**：工具调用缺乏统一标准，难以组合和复用
3. **维护困难**：每个项目都需要重新编写提示词和工具集成代码

**Agent Skills** 正是为了解决这些问题而诞生的。它是一套**标准化的能力封装规范**，将领域知识、工作流程和工具脚本打包成可复用的"技能包"。

### 核心定义

**Agent Skills** 是：

> 一种模块化、自包含的能力包，通过提供专业化的知识、工作流程和工具，扩展 AI 的能力。它就像特定领域或任务的"入职培训指南"，将 Claude 从通用智能体转变为具备专业知识的专家智能体。

### 技能 vs. 其他模式

为了更好地理解 Agent Skills，让我们对比一下它与传统方式的区别：

| 特性 | Agent Skills | System Prompt | Tool Calling |
|:---|:---|:---|:---|
| **触发方式** | 模型自动识别（基于语义匹配） | 始终加载 | 模型主动调用 |
| **加载时机** | 按需加载（渐进式） | 对话开始时加载 | 执行时调用 |
| **组织方式** | 标准化目录结构 | 文本块 | 函数/API |
| **可复用性** | 高（跨项目、跨团队） | 低（项目特定） | 中（需要集成） |
| **维护成本** | 低（独立维护） | 高（分散在各处） | 中（需要版本管理） |

### 一个简单的类比

想象一下：

- **System Prompt** = 员工手册（告诉员工基本规则）
- **Tool Calling** = 工具箱（提供各种工具）
- **Agent Skills** = **专业培训 + 工具箱 + 工作流程**（让员工成为某个领域的专家）

例如，一个 `maven-search` 技能不仅告诉 AI 如何搜索 Maven 依赖，还提供了：
- 搜索 API 的使用方法（知识）
- 标准化的搜索流程（工作流）
- 可执行的搜索脚本（工具）

---

## 为什么需要 Agent Skills？

### 问题场景

假设你是一个 Java 开发者，经常需要：

1. 查找 Maven 依赖的坐标
2. 检查依赖的最新版本
3. 生成 `pom.xml` 的依赖代码

**传统方式**：

每次都需要：
- 打开浏览器
- 访问 Maven Central
- 搜索依赖
- 复制坐标
- 手动编写 XML

这个过程需要 3-5 分钟，而且容易出错。

**使用 Agent Skills**：

只需要对 AI 说："帮我查找 Spring Boot 的最新版本"，AI 会自动：
1. 识别需要使用 `maven-search` 技能
2. 加载技能的工作流程
3. 执行搜索脚本
4. 返回格式化的结果

整个过程只需 5 秒钟，而且结果准确可靠。

### 核心价值

Agent Skills 带来的核心价值包括：

1. **效率提升**：将重复性工作从分钟级缩短到秒级
2. **质量保证**：通过标准化流程减少人为错误
3. **知识沉淀**：将专家经验代码化、工具化
4. **可复用性**：一次创建，处处使用
5. **可维护性**：独立维护，不影响其他功能

---

## 核心架构：渐进式披露机制

### 三层加载架构

Agent Skills 的核心创新在于**渐进式披露（Progressive Disclosure）**机制。它通过三层加载，在"强大能力"和"低延迟/节省 Token"之间取得平衡：

```
┌─────────────────────────────────────────┐
│  Level 1: 元数据（Metadata）              │
│  - 始终加载（~100 tokens）                │
│  - 用于技能路由和触发判断                  │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Level 2: 核心指令（SKILL.md）           │
│  - 技能触发后加载（<5k tokens）            │
│  - 包含工作流程和操作指南                  │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Level 3: 配套资源（Bundled Resources）  │
│  - 按需加载（scripts/references/assets）  │
│  - 提供工具和详细文档                     │
└─────────────────────────────────────────┘
```

### Level 1: 元数据（Metadata）

**作用**：技能的路由决策层

**内容**：YAML Frontmatter 中的 `name` 和 `description`

**特点**：
- 始终在上下文中（所有技能的元数据都会被加载）
- 非常精简（通常 50-100 词）
- 包含明确的触发条件

**示例**：

```yaml
---
name: maven-search
description: |
  Provides comprehensive guidance for searching and retrieving Maven 
  components from Maven Central Repository. Use when the user needs 
  to find, verify, or retrieve Maven dependencies, check component 
  versions, analyze dependency trees, or work with Maven coordinates.
---
```

**关键点**：
- `description` 是**唯一的触发机制**
- 必须包含"Use when..."明确触发条件
- 包含关键词和同义词（支持中英文）

### Level 2: 核心指令（SKILL.md Body）

**作用**：技能的行动纲领

**内容**：详细的工作流程、决策矩阵、操作步骤

**特点**：
- 技能触发后才加载
- 控制在 500 行以内（约 5k tokens）
- 包含核心逻辑，详细内容放在资源文件中

**示例结构**：

```markdown
# Maven Search Skill

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Searching for Maven dependencies
- Finding Maven coordinates
- Checking component versions

## How to use this skill

1. Identify the search type from user's request
2. Load the appropriate example from `examples/` directory
3. Execute the workflow using scripts
4. Present results in a clear format

## Best Practices

- Always validate coordinates
- Specify version explicitly
- Provide clear output
```

### Level 3: 配套资源（Bundled Resources）

**作用**：提供工具和详细文档

**内容**：
- `scripts/`：可执行脚本（Python/Bash 等）
- `references/`：参考文档（API 文档、规范等）
- `assets/`：静态资源（模板、图标等）

**特点**：
- 按需加载（Claude 决定何时读取）
- 可以很大（不受 5k tokens 限制）
- 脚本可以直接执行，无需加载到上下文

**示例**：

```
maven-search/
├── SKILL.md
├── scripts/
│   └── search_maven.py      # 搜索脚本
├── references/
│   └── maven-coordinates.md  # Maven 坐标规范
└── assets/
    └── pom-template.xml      # POM 模板
```

---

## 技能结构：从文件到能力

### 标准目录结构

一个符合规范的 Agent Skill 目录结构如下：

```
skill-name/
├── SKILL.md              # 必需：技能定义和说明
├── LICENSE.txt           # 必需：许可证文件
├── examples/             # 可选：使用示例
│   ├── example-1.md
│   └── example-2.md
├── api/                  # 可选：API 参考文档
│   └── api-reference.md
├── reference/           # 可选：领域知识库
│   ├── standards.md
│   └── best-practices.md
├── templates/            # 可选：输出模板
│   └── template-1.md
├── scripts/             # 可选：可执行脚本
│   └── script.py
└── assets/              # 可选：资源文件（不加载到上下文）
    └── logo.png
```

### SKILL.md 的结构

`SKILL.md` 是技能的核心文件，包含两部分：

#### 1. YAML Frontmatter（元数据）

```yaml
---
name: skill-name                    # 必需：技能名称（kebab-case）
description: |                      # 必需：技能描述（触发机制）
  Comprehensive description of what this skill does and when to use it.
  Use when the user needs to...
license: Complete terms in LICENSE.txt  # 可选：许可证说明
---
```

**关键要点**：
- `description` 是**唯一的触发机制**
- 必须包含明确的触发条件（"Use when..."）
- 包含关键词和同义词（中英文）

#### 2. Markdown Body（核心指令）

```markdown
# Skill Title

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- [明确的触发场景 1]
- [明确的触发场景 2]

## How to use this skill

1. **Identify the task type** from user's request
2. **Load the appropriate example** from `examples/` directory
3. **Follow the specific instructions** in that example
4. **Execute the workflow** using scripts or tools
5. **Present the results** in a clear format

## Best Practices

[最佳实践和注意事项]

## Keywords

**English keywords:**
[关键词列表]

**Chinese keywords:**
[中文关键词列表]
```

### 资源文件的用途

#### Scripts（脚本）

**用途**：执行确定性任务或重复性代码

**何时包含**：
- 需要确定性执行（如数学计算、格式转换）
- 相同代码被重复编写

**示例**：

```python
#!/usr/bin/env python3
"""Maven Central Repository 搜索脚本"""
import requests
import json
import sys

def search_maven(query, limit=10):
    """搜索 Maven Central Repository"""
    url = "https://search.maven.org/solrsearch/select"
    params = {"q": query, "rows": limit, "wt": "json"}
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    query = sys.argv[1]
    results = search_maven(query)
    print(json.dumps(results, indent=2))
```

#### References（参考文档）

**用途**：提供领域知识和详细文档

**何时包含**：
- API 文档、规范文档
- 业务逻辑、架构图
- 公司政策、模板

**示例**：

```markdown
# Maven 坐标参考

## 坐标格式

Maven 坐标由三部分组成：
- `groupId`：组织标识
- `artifactId`：项目标识
- `version`：版本号

## 版本规范

- **发布版本**：遵循语义化版本（SemVer）
- **快照版本**：以 `-SNAPSHOT` 结尾
```

#### Assets（资源文件）

**用途**：提供输出模板和静态资源

**何时包含**：
- 代码模板、文档模板
- 品牌 Logo、图标
- 字体文件

**特点**：
- **不加载到上下文**（节省 Token）
- 直接用于输出（复制或修改）

---

## 创建你的第一个技能

### 场景：创建一个"代码审查"技能

假设你经常需要让 AI 审查代码，希望它遵循特定的审查标准。让我们创建一个 `code-review` 技能。

### 步骤 1：创建目录结构

```bash
mkdir -p code-review/{examples,reference,scripts}
cd code-review
```

### 步骤 2：创建 SKILL.md

```markdown
---
name: code-review
description: |
  Provides comprehensive code review guidance following industry best practices.
  Use when the user asks for code review, code quality check, or code improvement
  suggestions. This skill covers security, performance, maintainability, and
  best practices for various programming languages.
license: Complete terms in LICENSE.txt
---

# Code Review Skill

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Code review
- Code quality check
- Code improvement
- Code refactoring suggestions
- Security vulnerabilities
- Performance issues
- Code style violations

**Trigger phrases include:**
- "审查这段代码" (review this code)
- "检查代码质量" (check code quality)
- "代码有什么问题" (what's wrong with this code)
- "如何改进这段代码" (how to improve this code)

## How to use this skill

**CRITICAL: This skill should be triggered when the user provides code and asks for review or improvement.**

1. **Identify the programming language** from the code
2. **Load the appropriate review checklist** from `reference/` directory
3. **Analyze the code** against the checklist:
   - Security vulnerabilities
   - Performance issues
   - Code style and maintainability
   - Best practices
4. **Provide structured feedback**:
   - Critical issues (must fix)
   - Warnings (should fix)
   - Suggestions (nice to have)
5. **Provide code examples** for improvements when applicable

## Review Checklist

Refer to `reference/review-checklist.md` for detailed checklists by language.

## Best Practices

1. **Be constructive**: Focus on improvement, not criticism
2. **Prioritize issues**: Critical > Warning > Suggestion
3. **Provide examples**: Show how to fix issues
4. **Consider context**: Understand the code's purpose before reviewing

## Keywords

**English keywords:**
code review, code quality, code inspection, code analysis, refactoring, security audit, performance review, code style, best practices, code smell, technical debt

**Chinese keywords:**
代码审查, 代码质量, 代码检查, 代码分析, 重构, 安全审计, 性能审查, 代码风格, 最佳实践, 代码异味, 技术债务
```

### 步骤 3：创建参考文档

**reference/review-checklist.md**：

```markdown
# Code Review Checklist

## Security

- [ ] Input validation
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] Authentication and authorization
- [ ] Sensitive data exposure
- [ ] Dependency vulnerabilities

## Performance

- [ ] Algorithm efficiency
- [ ] Database query optimization
- [ ] Caching strategies
- [ ] Resource cleanup
- [ ] Memory leaks

## Maintainability

- [ ] Code readability
- [ ] Function complexity
- [ ] Code duplication
- [ ] Naming conventions
- [ ] Documentation
```

### 步骤 4：创建示例

**examples/java-review.md**：

```markdown
# Java Code Review Example

## Input

```java
public String getUserData(int userId) {
    String sql = "SELECT * FROM users WHERE id = " + userId;
    return db.execute(sql);
}
```

## Review Points

1. **Security**: SQL injection vulnerability
2. **Best Practice**: Use prepared statements
3. **Return Type**: Should return User object, not String

## Improved Code

```java
public User getUserData(int userId) {
    String sql = "SELECT * FROM users WHERE id = ?";
    PreparedStatement stmt = connection.prepareStatement(sql);
    stmt.setInt(1, userId);
    ResultSet rs = stmt.executeQuery();
    // Map result to User object
    return userMapper.map(rs);
}
```
```

### 步骤 5：创建许可证文件

**LICENSE.txt**：

```
Apache License 2.0
[完整的许可证文本]
```

### 步骤 6：测试技能

1. 将技能目录放到 Claude 的技能目录（如 `~/.claude/skills/`）
2. 在对话中测试："请审查这段代码：[代码]"
3. 观察 AI 是否自动触发了 `code-review` 技能

---

## 架构师的最佳实践

### 1. 精心编写 Description

`description` 是技能的唯一触发机制，必须精心设计：

**好的示例**：

```yaml
description: |
  Provides comprehensive guidance for searching and retrieving Maven 
  components from Maven Central Repository. Use when the user needs 
  to find, verify, or retrieve Maven dependencies, check component 
  versions, analyze dependency trees, or work with Maven coordinates.
```

**不好的示例**：

```yaml
description: Maven search tool  # 太简单，缺乏触发条件
```

**设计原则**：
- 包含"Use when..."明确触发条件
- 包含关键词和同义词（中英文）
- 描述技能的核心功能和边界

### 2. 保持 SKILL.md 精简

**原则**：Claude 已经很聪明，只添加它不知道的信息

**做法**：
- 控制在 500 行以内
- 详细内容放在 `reference/` 或 `examples/` 中
- 使用命令式/不定式（imperative/infinitive form）

**示例**：

```markdown
# 好的写法
Extract text with pdfplumber. See [FORMS.md](reference/FORMS.md) for form filling.

# 不好的写法
This skill uses pdfplumber library which is a Python library for extracting 
text from PDF files. It supports various features including form filling, 
text extraction, and more. For form filling, you need to...
```

### 3. 模块化设计

**原则**：不要创建"万能技能"，遵循单一职责原则

**好的设计**：
- `git-standard-commit`：标准化 Git 提交
- `jira-issue-updater`：更新 Jira 工单
- `maven-search`：搜索 Maven 依赖

**不好的设计**：
- `developer-toolkit`：包含所有开发工具（太大、难以触发）

### 4. 将确定性交给脚本

**原则**：LLM 擅长推理，但不擅长精确计算

**做法**：
- 复杂的数学计算 → 使用脚本
- 格式转换 → 使用脚本
- API 调用 → 使用脚本

**示例**：

```python
# 使用脚本计算，而不是让 AI 计算
def calculate_compound_interest(principal, rate, years):
    return principal * (1 + rate) ** years
```

### 5. 渐进式信息披露

**原则**：按需加载，节省 Token

**做法**：
- 核心逻辑在 SKILL.md
- 详细文档在 `reference/`
- 示例在 `examples/`
- 模板在 `assets/`

### 6. 存储策略

**个人级技能**：
- 路径：`~/.claude/skills/`
- 用途：跨项目使用
- 示例：个人工具、通用技能

**项目级技能**：
- 路径：`.claude/skills/`（项目根目录）
- 用途：团队共享
- 示例：项目特定的工作流程、公司规范

---

## 常见问题与解决方案

### Q1: 技能没有被触发怎么办？

**可能原因**：
1. `description` 不够明确
2. 关键词不匹配
3. 技能未正确安装

**解决方案**：
1. 优化 `description`，添加更多触发关键词
2. 检查技能是否在正确的目录
3. 查看 Claude 的日志，了解为什么没有触发

### Q2: 技能被错误触发怎么办？

**可能原因**：
1. `description` 太宽泛
2. 与其他技能冲突

**解决方案**：
1. 缩小技能范围，使 `description` 更具体
2. 检查是否有其他技能有相似的 `description`
3. 使用更明确的触发条件

### Q3: SKILL.md 太长怎么办？

**解决方案**：
1. 将详细内容移到 `reference/` 目录
2. 使用链接引用其他文件
3. 只保留核心工作流程

**示例**：

```markdown
# 核心工作流程
1. Identify task type
2. Load appropriate reference: See [API.md](reference/API.md)
3. Execute workflow
```

### Q4: 如何测试技能？

**方法**：
1. **手动测试**：在对话中尝试触发技能
2. **单元测试**：测试脚本的功能
3. **集成测试**：测试技能在真实场景中的表现

### Q5: 技能可以调用外部 API 吗？

**可以**，但需要注意：

1. **使用脚本**：将 API 调用封装在脚本中
2. **错误处理**：处理网络错误、超时等
3. **安全性**：不要在技能中硬编码 API 密钥

**示例**：

```python
import os
import requests

def call_api(endpoint, params):
    api_key = os.getenv('API_KEY')  # 从环境变量读取
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(endpoint, params=params, headers=headers)
    return response.json()
```

---

## 下一步学习

### 推荐资源

1. **官方文档**：
   - [Agent Skills 规范](https://agentskills.io/)
   - [Claude Skills 开发指南](https://support.claude.com/zh-CN/articles/12512198)
   - [Agent Skills 规范文档](https://agentskills.io/specification)

2. **示例技能**：
   - 浏览 [full-stack-skills](https://github.com/partme-ai/full-stack-skills) 仓库
   - 学习现有技能的实现方式
   - 参考 `mermaid`、`maven-search` 等技能

3. **最佳实践**：
   - 阅读 `skill-creator` 技能的详细指南
   - 参与社区讨论
   - 贡献自己的技能

### 实践建议

1. **从简单开始**：先创建一个简单的技能，熟悉流程
2. **迭代改进**：根据使用反馈不断优化技能
3. **分享经验**：将你的技能分享给社区
4. **持续学习**：关注 Agent Skills 规范的最新更新

### 进阶主题

- **技能编排**：如何组合多个技能完成复杂任务
- **性能优化**：如何减少 Token 消耗，提升响应速度
- **安全控制**：如何确保技能的安全性
- **质量保证**：如何测试和评估技能的质量

---

## 总结

Agent Skills 不仅仅是一种功能扩展方式，更是一种**从"指令驱动"向"能力工程"演进的范式转变**。它通过标准化的能力封装，让 AI 能够：

1. **自动识别**：根据用户需求自动选择合适的技能
2. **按需加载**：通过渐进式披露机制，平衡能力和效率
3. **专业执行**：将通用 AI 转变为领域专家

作为架构师，掌握 Agent Skills 是构建企业级 AI 应用的必经之路。通过精心设计的技能，我们可以：

- **提升效率**：将重复性工作自动化
- **保证质量**：通过标准化流程减少错误
- **沉淀知识**：将专家经验代码化、工具化

现在，开始创建你的第一个 Agent Skill 吧！

---

**文档版本**：1.0.0  
**最后更新**：2024-12-19  
**维护者**：Full-Stack-Skills Team

**相关资源**：
- [Agent Skills 规范](https://agentskills.io/)
- [Claude Skills 开发指南](https://support.claude.com/zh-CN/articles/12512198)
- [Full-Stack-Skills 仓库](https://github.com/partme-ai/full-stack-skills)
