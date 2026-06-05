# 异常日志规约

## 目录
- [一、错误码](#一错误码)
- [二、异常处理](#二异常处理)
- [三、日志规约](#三日志规约)

---

## 一、错误码

### 【强制】规约

1. **错误码制定原则**：快速溯源、沟通标准化

2. **错误码不体现版本号和错误等级**

3. **全部正常返回00000**

4. **错误码格式**：5位字符串 = 错误来源(1位) + 数字编号(4位)

   | 来源 | 含义 | 说明 |
   |------|------|------|
   | A | 用户端错误 | 参数错误、版本过低、支付超时等 |
   | B | 当前系统错误 | 业务逻辑出错、程序健壮性差等 |
   | C | 第三方服务错误 | CDN出错、消息投递超时等 |

5. **编号先到先得**，不与业务/组织架构挂钩

6. **避免随意定义新错误码**，优先使用已有错误码

7. **错误码不直接输出给用户**

### 【推荐】规约

- 业务独特信息由errorMessage承载
- 第三方错误码可转义（C→B），带上原错误码

### 【参考】规约

- 一级宏观错误码：`A0001`(用户端错误) / `B0001`(系统执行出错) / `C0001`(调用第三方出错)

### 常用错误码示例

| 错误码 | 描述 |
|--------|------|
| 00000 | 一切OK |
| A0001 | 用户端错误 |
| A0100 | 用户注册错误 |
| A0111 | 用户名已存在 |
| A0121 | 密码长度不够 |
| B0001 | 系统执行出错 |
| C0001 | 调用第三方服务出错 |

---

## 二、异常处理

### 【强制】规约

1. **预检查规避RuntimeException**：
   ```java
   // 正例
   if (obj != null) { obj.method(); }
   // 反例
   try { obj.method(); } catch (NullPointerException e) { }
   ```

2. **异常不用于流程控制**：效率比条件判断低很多

3. **catch区分异常类型**：对非稳定代码分类处理

4. **捕获后必须处理**：
   - 不能空处理
   - 不处理则向上抛出
   - 最外层必须转化为用户可理解内容

5. **事务场景注意手动回滚**

6. **finally块关闭资源**：
   ```java
   // JDK7+ 推荐
   try (InputStream is = new FileInputStream(file)) {
       // ...
   }
   ```

7. **禁止在finally中使用return**：
   ```java
   // 反例：会丢弃try中的return
   private int x = 0;
   public int checkReturn() {
       try { return ++x; }
       finally { return ++x; }  // 返回2而非1
   }
   ```

8. **捕获异常与抛出异常匹配**（或是父类）

9. **RPC/动态类用Throwable拦截**

### 【推荐】规约

1. **返回null时必须注释说明**

2. **防止NPE的场景**：
   - 返回基本类型但return包装对象
   - 数据库查询结果
   - 集合元素即使isNotEmpty也可能为null
   - 远程调用返回对象
   - Session获取的数据
   - 级联调用`obj.getA().getB().getC()`

3. **使用自定义异常**：
   - 推荐：`DAOException` / `ServiceException`
   - 避免：直接抛`RuntimeException` / `Exception` / `Throwable`

### 【参考】规约

**RPC返回方式选择**：
- 公司外HTTP/API接口：使用errorCode
- 应用内部：异常抛出
- 跨应用RPC：Result方式封装

```java
// Result方式示例
public class Result<T> {
    private boolean success;
    private String errorCode;
    private String errorMessage;
    private T data;
}
```

---

## 三、日志规约

### 【强制】规约

1. **使用日志框架SLF4J**，不直接用Log4j/Logback：
   ```java
   import org.slf4j.Logger;
   import org.slf4j.LoggerFactory;
   private static final Logger logger = LoggerFactory.getLogger(Test.class);
   ```

2. **日志保存时间**：
   - 至少15天（异常可能"周"为频次）
   - 敏感操作日志不少于6个月（法规要求）

3. **日志文件命名**：
   - 当天：`应用名.log`
   - 历史：`应用名.log.yyyy-MM-dd`
   - 路径：`/home/admin/应用名/logs/`

4. **扩展日志命名**：`appName_logType_logName.log`

5. **字符串拼接用占位符**：
   ```java
   // 正例
   logger.debug("Processing trade with id: {} and symbol: {}", id, symbol);
   ```

6. **trace/debug/info必须级别判断**：
   ```java
   if (logger.isDebugEnabled()) {
       logger.debug("Current ID is: {} and name is: {}", id, getName());
   }
   ```

7. **避免重复打印**：设置`additivity=false`

8. **生产环境禁止**：
   - `System.out` / `System.err`
   - `e.printStackTrace()`

9. **异常日志包含**：案发现场信息 + 异常堆栈
   ```java
   logger.error("inputParams:{} and errorMessage:{}",
       params, e.getMessage(), e);
   ```

10. **禁止直接JSON工具转换对象**

### 【推荐】规约

1. **谨慎记录日志**：
   - 生产禁止debug日志
   - 有选择输出info日志
   - warn注意输出量

2. **参数错误用warn**，不用error

3. **日志语言**：英文优先，说不清用中文
