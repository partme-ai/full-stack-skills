---
name: spring-ai-alibaba
description: "Provides comprehensive guidance for Spring AI Alibaba including Alibaba Cloud AI services integration, model APIs, and AI application development. Use when the user asks about Spring AI Alibaba, needs to use Alibaba Cloud AI services, or integrate AI capabilities in Spring applications."
---

# Spring AI Alibaba 开发指南

## 概述

Spring AI Alibaba 提供了与阿里云 DashScope（通义千问）的集成，支持使用阿里云的大语言模型服务。

## 核心功能

### 1. 项目创建

**依赖**：

```xml
<dependency>
    <groupId>com.alibaba.cloud.ai</groupId>
    <artifactId>spring-ai-starter-model-aliyun-dashscope</artifactId>
</dependency>
```

**或使用 Gradle**：

```gradle
dependencies {
    implementation 'com.alibaba.cloud.ai:spring-ai-starter-model-aliyun-dashscope'
}
```

### 2. 配置

**application.yml**：

```yaml
spring:
  ai:
    alibaba:
      dashscope:
        api-key: ${DASHSCOPE_API_KEY}
        chat:
          options:
            model: qwen-turbo
            temperature: 0.7
            max-tokens: 2000
```

**application.properties**：

```properties
spring.ai.alibaba.dashscope.api-key=${DASHSCOPE_API_KEY}
spring.ai.alibaba.dashscope.chat.options.model=qwen-turbo
spring.ai.alibaba.dashscope.chat.options.temperature=0.7
spring.ai.alibaba.dashscope.chat.options.max-tokens=2000
```

### 3. Chat Client

**使用 ChatClient**：

```java
@Service
public class ChatService {
    private final ChatClient chatClient;
    
    public ChatService(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    public String chat(String message) {
        return chatClient.call(message);
    }
    
    public String chatWithPrompt(String userMessage) {
        Prompt prompt = new Prompt(new UserMessage(userMessage));
        ChatResponse response = chatClient.call(prompt);
        return response.getResult().getOutput().getContent();
    }
}
```

**流式响应**：

```java
@Service
public class ChatService {
    private final StreamingChatClient streamingChatClient;
    
    public ChatService(StreamingChatClient streamingChatClient) {
        this.streamingChatClient = streamingChatClient;
    }
    
    public Flux<String> streamChat(String message) {
        return streamingChatClient.stream(message)
            .map(response -> response.getResult().getOutput().getContent());
    }
}
```

### 4. 模型选择

**支持的模型**：

- `qwen-turbo` - 通义千问 Turbo 模型（快速响应）
- `qwen-plus` - 通义千问 Plus 模型（平衡性能）
- `qwen-max` - 通义千问 Max 模型（最强性能）

**配置不同模型**：

```yaml
spring:
  ai:
    alibaba:
      dashscope:
        chat:
          options:
            model: qwen-max  # 使用最强模型
            temperature: 0.7
            max-tokens: 2000
```

### 5. Prompt Template

**定义模板**：

```java
@Service
public class PromptService {
    private final PromptTemplate promptTemplate;
    
    public PromptService() {
        this.promptTemplate = new PromptTemplate(
            "请用{style}风格回答以下问题：{question}"
        );
    }
    
    public String generatePrompt(String style, String question) {
        Map<String, Object> variables = Map.of(
            "style", style,
            "question", question
        );
        return promptTemplate.render(variables);
    }
}
```

**使用 ChatClient**：

```java
@Service
public class ChatService {
    private final ChatClient chatClient;
    private final PromptTemplate promptTemplate;
    
    public ChatService(ChatClient chatClient) {
        this.chatClient = chatClient;
        this.promptTemplate = new PromptTemplate(
            "请用{style}风格回答以下问题：{question}"
        );
    }
    
    public String chatWithStyle(String style, String question) {
        Prompt prompt = promptTemplate.create(Map.of(
            "style", style,
            "question", question
        ));
        ChatResponse response = chatClient.call(prompt);
        return response.getResult().getOutput().getContent();
    }
}
```

### 6. Embedding

**配置**：

```yaml
spring:
  ai:
    alibaba:
      dashscope:
        embedding:
          options:
            model: text-embedding-V1
```

**使用 EmbeddingClient**：

```java
@Service
public class EmbeddingService {
    private final EmbeddingClient embeddingClient;
    
    public EmbeddingService(EmbeddingClient embeddingClient) {
        this.embeddingClient = embeddingClient;
    }
    
    public List<Double> embed(String text) {
        EmbeddingResponse response = embeddingClient.embedForResponse(
            List.of(text)
        );
        return response.getResult().getOutput();
    }
    
    public List<List<Double>> embedBatch(List<String> texts) {
        EmbeddingResponse response = embeddingClient.embedForResponse(texts);
        return response.getResult().getOutput();
    }
}
```

### 7. 多轮对话

**维护对话上下文**：

```java
@Service
public class ConversationService {
    private final ChatClient chatClient;
    private final List<Message> conversationHistory = new ArrayList<>();
    
    public ConversationService(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    public String chat(String userMessage) {
        conversationHistory.add(new UserMessage(userMessage));
        
        Prompt prompt = new Prompt(conversationHistory);
        ChatResponse response = chatClient.call(prompt);
        String assistantMessage = response.getResult().getOutput().getContent();
        
        conversationHistory.add(new AssistantMessage(assistantMessage));
        return assistantMessage;
    }
    
    public void clearHistory() {
        conversationHistory.clear();
    }
}
```

## 最佳实践

### 1. 配置管理

- 使用环境变量存储 API Key
- 区分开发和生产环境配置
- 配置合理的超时和重试策略

### 2. 错误处理

```java
@Service
public class ChatService {
    private final ChatClient chatClient;
    
    public String chat(String message) {
        try {
            return chatClient.call(message);
        } catch (Exception e) {
            // 处理错误
            log.error("Chat error", e);
            return "抱歉，处理请求时出现错误";
        }
    }
}
```

### 3. 性能优化

- 根据场景选择合适的模型（turbo/plus/max）
- 使用流式响应提升用户体验
- 合理使用缓存减少 API 调用

### 4. 成本控制

- 选择合适的模型（qwen-turbo 成本更低）
- 限制 Token 使用量
- 监控 API 调用情况

### 5. 中文优化

通义千问对中文支持较好，可以：

- 使用中文 Prompt 模板
- 优化中文提示词
- 利用多轮对话能力

## 常用依赖

```xml
<!-- Spring AI Alibaba DashScope -->
<dependency>
    <groupId>com.alibaba.cloud.ai</groupId>
    <artifactId>spring-ai-starter-model-aliyun-dashscope</artifactId>
</dependency>

<!-- Spring Boot Web (可选，用于 REST API) -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

## 配置示例

**完整配置**：

```yaml
spring:
  ai:
    alibaba:
      dashscope:
        api-key: ${DASHSCOPE_API_KEY}
        chat:
          options:
            model: qwen-turbo
            temperature: 0.7
            max-tokens: 2000
            top-p: 0.9
        embedding:
          options:
            model: text-embedding-V1
```

## 示例 Prompt

- "如何使用 Spring AI Alibaba 集成通义千问？"
- "Spring AI Alibaba 中如何配置不同的模型？"
- "如何在 Spring AI Alibaba 中实现流式响应？"
- "Spring AI Alibaba 中如何实现多轮对话？"
- "如何优化 Spring AI Alibaba 的中文处理能力？"
