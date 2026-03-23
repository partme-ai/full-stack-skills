---
name: spring-ai
description: Provides comprehensive guidance for Spring AI including AI model integration, prompt templates, vector stores, and AI applications. Use when the user asks about Spring AI, needs to integrate AI models, implement RAG applications, or work with AI services in Spring.
---

# Spring AI 开发指南

## 概述

Spring AI 是 Spring 官方提供的 AI 应用开发框架，简化了与各种大语言模型（LLM）的集成，包括 OpenAI、Anthropic、Azure OpenAI 等。

## 核心功能

### 1. 项目创建

**依赖**：

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
</dependency>
```

**或使用 Gradle**：

```gradle
dependencies {
    implementation 'org.springframework.ai:spring-ai-openai-spring-boot-starter'
}
```

### 2. Chat Client

**配置**：

```yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
      chat:
        options:
          model: gpt-4
          temperature: 0.7
```

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

### 3. Prompt Template

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

### 4. Embedding

**配置**：

```yaml
spring:
  ai:
    openai:
      embedding:
        options:
          model: text-embedding-ada-002
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

### 5. Vector Store

**配置**：

```yaml
spring:
  ai:
    vectorstore:
      pgvector:
        index-type: HNSW
        distance-type: COSINE_DISTANCE
```

**使用 VectorStore**：

```java
@Service
public class VectorStoreService {
    private final VectorStore vectorStore;
    private final EmbeddingClient embeddingClient;
    
    public VectorStoreService(
        VectorStore vectorStore,
        EmbeddingClient embeddingClient
    ) {
        this.vectorStore = vectorStore;
        this.embeddingClient = embeddingClient;
    }
    
    public void addDocument(String id, String content) {
        List<Double> embedding = embeddingClient.embed(content);
        Document document = new Document(id, content, Map.of());
        vectorStore.add(List.of(document));
    }
    
    public List<Document> searchSimilar(String query, int topK) {
        List<Double> queryEmbedding = embeddingClient.embed(query);
        return vectorStore.similaritySearch(
            SearchRequest.query(query)
                .withTopK(topK)
        );
    }
}
```

### 6. Function Calling

**定义函数**：

```java
@Bean
public Function<WeatherRequest, WeatherResponse> weatherFunction() {
    return request -> {
        // 调用天气 API
        WeatherResponse response = weatherService.getWeather(
            request.getLocation()
        );
        return response;
    };
}
```

**配置 Function Calling**：

```java
@Configuration
public class FunctionCallingConfig {
    @Bean
    public Function<WeatherRequest, WeatherResponse> weatherFunction() {
        return request -> {
            // 实现天气查询逻辑
            return new WeatherResponse(/* ... */);
        };
    }
}
```

**使用 Function Calling**：

```java
@Service
public class ChatService {
    private final ChatClient chatClient;
    private final FunctionCallbackRegistry functionCallbackRegistry;
    
    public ChatService(
        ChatClient chatClient,
        FunctionCallbackRegistry functionCallbackRegistry
    ) {
        this.chatClient = chatClient;
        this.functionCallbackRegistry = functionCallbackRegistry;
    }
    
    public String chatWithFunction(String message) {
        Prompt prompt = new Prompt(
            new UserMessage(message),
            functionCallbackRegistry.getFunctionCallbacks()
        );
        ChatResponse response = chatClient.call(prompt);
        return response.getResult().getOutput().getContent();
    }
}
```

### 7. 多模型支持

**配置多个模型**：

```yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
    anthropic:
      api-key: ${ANTHROPIC_API_KEY}
    azure:
      openai:
        api-key: ${AZURE_OPENAI_API_KEY}
        endpoint: ${AZURE_OPENAI_ENDPOINT}
```

**使用特定模型**：

```java
@Service
public class MultiModelService {
    private final ChatClient openAiChatClient;
    private final ChatClient anthropicChatClient;
    
    public MultiModelService(
        @Qualifier("openAiChatClient") ChatClient openAiChatClient,
        @Qualifier("anthropicChatClient") ChatClient anthropicChatClient
    ) {
        this.openAiChatClient = openAiChatClient;
        this.anthropicChatClient = anthropicChatClient;
    }
    
    public String chatWithOpenAI(String message) {
        return openAiChatClient.call(message);
    }
    
    public String chatWithAnthropic(String message) {
        return anthropicChatClient.call(message);
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

- 使用流式响应提升用户体验
- 合理使用缓存减少 API 调用
- 批量处理 Embedding 请求

### 4. 成本控制

- 选择合适的模型（GPT-3.5 vs GPT-4）
- 限制 Token 使用量
- 监控 API 调用情况

## 常用依赖

```xml
<!-- OpenAI -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
</dependency>

<!-- Anthropic -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-anthropic-spring-boot-starter</artifactId>
</dependency>

<!-- Azure OpenAI -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-azure-openai-spring-boot-starter</artifactId>
</dependency>

<!-- Vector Store (PGVector) -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-pgvector-store-spring-boot-starter</artifactId>
</dependency>
```

## 示例 Prompt

- "如何使用 Spring AI 集成 OpenAI？"
- "Spring AI 中如何实现流式响应？"
- "如何在 Spring AI 中使用 Embedding 和 Vector Store？"
- "Spring AI 中如何实现 Function Calling？"
- "如何配置 Spring AI 支持多个模型？"
