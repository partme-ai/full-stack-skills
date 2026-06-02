# 安全规约

## 目录
- [权限控制](#权限控制)
- [数据脱敏](#数据脱敏)
- [SQL注入防护](#sql注入防护)
- [参数校验](#参数校验)
- [XSS防护](#xss防护)
- [CSRF防护](#csrf防护)
- [URL重定向安全](#url重定向安全)
- [防重放机制](#防重放机制)

---

## 权限控制

### 【强制】隶属于用户个人的页面或功能必须进行权限控制校验

```java
// 正例：水平权限校验
public void viewMessage(Long messageId, Long userId) {
    Message message = messageDao.getById(messageId);
    if (!message.getUserId().equals(userId)) {
        throw new PermissionDeniedException("无权访问");
    }
}
```

**风险场景**：查看他人私信、修改他人订单、删除他人数据

---

## 数据脱敏

### 【强制】用户敏感数据禁止直接展示，必须脱敏

```java
public class DataMaskUtil {
    // 手机号脱敏：139****1219
    public static String maskPhone(String phone) {
        return phone.substring(0, 3) + "****" + phone.substring(phone.length() - 4);
    }

    // 身份证脱敏：110***********1234
    public static String maskIdCard(String idCard) {
        return idCard.substring(0, 3) + "***********" + idCard.substring(idCard.length() - 4);
    }

    // 银行卡脱敏：6222 **** **** 1234
    public static String maskBankCard(String cardNo) {
        return cardNo.substring(0, 4) + " **** **** " + cardNo.substring(cardNo.length() - 4);
    }
}
```

---

## SQL注入防护

### 【强制】用户输入的SQL参数严格使用参数绑定

```java
// 正例：使用PreparedStatement
public User findByUsername(String username) {
    String sql = "SELECT * FROM user WHERE username = ?";
    return jdbcTemplate.queryForObject(sql, new Object[]{username}, userRowMapper);
}

// 反例：字符串拼接SQL
public User findByUsername(String username) {
    String sql = "SELECT * FROM user WHERE username = '" + username + "'";
    // 危险！
}
```

**MyBatis正确用法**：
- `#{param}` 安全
- `${param}` 不安全，易注入

---

## 参数校验

### 【强制】用户请求传入的任何参数必须做有效性验证

**忽略参数校验可能导致**：
- `page size`过大导致内存溢出
- 恶意`order by`导致数据库慢查询
- 缓存击穿、SSRF、SQL注入、ReDoS

```java
// 正例：参数校验
public PageResult<User> listUsers(UserQuery query) {
    // 分页参数校验
    if (query.getPageNum() == null || query.getPageNum() < 1) {
        query.setPageNum(1);
    }
    if (query.getPageSize() == null || query.getPageSize() > 100) {
        query.setPageSize(20);
    }
    // 排序字段白名单
    if (!ALLOWED_ORDER_FIELDS.contains(query.getOrderBy())) {
        throw new IllegalArgumentException("非法排序字段");
    }
    return userDao.queryPage(query);
}
```

---

## XSS防护

### 【强制】禁止向HTML页面输出未经安全过滤的用户数据

```java
import org.apache.commons.text.StringEscapeUtils;

public String safeOutput(String userInput) {
    return StringEscapeUtils.escapeHtml4(userInput);
}
```

---

## CSRF防护

### 【强制】表单、AJAX提交必须执行CSRF安全验证

```java
@Controller
public class CsrfController {

    @GetMapping("/form")
    public String showForm(HttpSession session, Model model) {
        String csrfToken = UUID.randomUUID().toString();
        session.setAttribute("csrfToken", csrfToken);
        model.addAttribute("csrfToken", csrfToken);
        return "form";
    }

    @PostMapping("/submit")
    public String submitForm(HttpSession session, @RequestParam String csrfToken) {
        String sessionToken = (String) session.getAttribute("csrfToken");
        if (!csrfToken.equals(sessionToken)) {
            throw new SecurityException("CSRF验证失败");
        }
        return "success";
    }
}
```

---

## URL重定向安全

### 【强制】URL外部重定向必须执行白名单过滤

```java
public class RedirectUtil {
    private static final Set<String> ALLOWED_DOMAINS = Set.of(
        "www.example.com", "m.example.com"
    );

    public static String safeRedirect(String targetUrl) {
        try {
            URL url = new URL(targetUrl);
            if (!ALLOWED_DOMAINS.contains(url.getHost())) {
                return "/";
            }
            return targetUrl;
        } catch (MalformedURLException e) {
            return "/";
        }
    }
}
```

---

## 防重放机制

### 【强制】使用平台资源必须实现防重放机制

适用场景：短信、邮件、电话、下单、支付

```java
@Service
public class SmsService {
    // 发送频率限制：1分钟1次
    private static final int INTERVAL_SECONDS = 60;
    // 日发送次数限制：10次
    private static final int DAILY_LIMIT = 10;

    public void sendVerifyCode(String phone) {
        String intervalKey = "sms:interval:" + phone;

        // 频率限制
        if (redisTemplate.hasKey(intervalKey)) {
            throw new BusinessException("发送过于频繁");
        }

        // 日次数限制
        Long count = redisTemplate.opsForValue().increment("sms:daily:" + phone);
        if (count > DAILY_LIMIT) {
            throw new BusinessException("今日发送次数已达上限");
        }

        // 发送验证码...

        redisTemplate.opsForValue().set(intervalKey, "1",
            Duration.ofSeconds(INTERVAL_SECONDS));
    }
}
```
