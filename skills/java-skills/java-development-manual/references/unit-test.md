# 单元测试规约

## 目录
- [AIR原则](#air原则)
- [BCDE原则](#bcde原则)
- [强制规约](#强制规约)
- [推荐规约](#推荐规约)
- [测试代码示例](#测试代码示例)

---

## AIR原则

好的单元测试必须遵守AIR原则：

| 原则 | 含义 | 说明 |
|------|------|------|
| **A**utomatic | 自动化 | 测试执行完全自动化，非交互式 |
| **I**ndependent | 独立性 | 测试用例间不互相调用，不依赖执行顺序 |
| **R**epeatable | 可重复 | 不受外界环境影响，可重复执行 |

---

## BCDE原则

编写单元测试遵守BCDE原则：

| 原则 | 含义 | 说明 |
|------|------|------|
| **B**order | 边界值测试 | 循环边界、特殊取值、特殊时间点、数据顺序 |
| **C**orrect | 正确性测试 | 正确输入得到预期结果 |
| **D**esign | 设计结合 | 与设计文档结合编写测试 |
| **E**rror | 错误测试 | 非法数据、异常流程、业务允许外的情况 |

---

## 强制规约

### 1. 测试自动化

- 测试必须全自动执行，非交互式
- **禁止**使用`System.out`人肉验证
- **必须**使用assert验证结果

### 2. 测试独立性

- 测试用例间**不能互相调用**
- **不能依赖执行顺序**

### 3. 测试可重复性

- 不受外部环境影响（网络、服务、中间件）
- 通过DI注入本地/Mock实现

### 4. 测试粒度

- 至多是**类级别**，一般是**方法级别**
- 单测不负责跨类/跨系统的交互逻辑

### 5. 核心业务增量代码必须单测通过

### 6. 测试代码目录

- **必须**写在`src/test/java`
- **禁止**写在业务代码目录下

---

## 推荐规约

### 1. 测试覆盖率目标

| 类型 | 语句覆盖率 | 分支覆盖率 |
|------|-----------|-----------|
| 一般代码 | 70% | - |
| 核心模块 | 100% | 100% |

**重点测试**：DAO层、Manager层、可重用度高的Service

### 2. 数据库测试

- **不假设**数据库数据存在
- **不直接操作**数据库插入数据
- 使用**程序插入**或**导入数据**方式准备

### 3. 数据库测试数据隔离

- 设定**自动回滚**机制
- 或用**明确前缀标识**测试数据

### 4. 可测性设计

避免以下情况：
- 构造方法做太多事情
- 过多全局变量和静态方法
- 过多外部依赖
- 过多条件语句

### 5. 测试时机

- **项目提测前**完成单元测试
- **不建议**项目发布后补充

---

## 测试代码示例

```java
/**
 * UserService单元测试
 */
@RunWith(SpringRunner.class)
@SpringBootTest
public class UserServiceTest {

    @Autowired
    private UserService userService;

    @MockBean
    private ExternalApiService externalApiService;

    private User testUser;

    @Before
    public void setUp() {
        testUser = new User();
        testUser.setUsername("test_user_" + System.currentTimeMillis());
    }

    @After
    public void tearDown() {
        if (testUser.getId() != null) {
            userService.delete(testUser.getId());
        }
    }

    // 正常流程测试 (Correct)
    @Test
    public void testCreateUser_success() {
        UserDTO dto = new UserDTO();
        dto.setUsername("newuser");

        Long userId = userService.createUser(dto);

        assertNotNull(userId);
    }

    // 边界值测试 (Border)
    @Test(expected = IllegalArgumentException.class)
    public void testCreateUser_usernameTooLong() {
        UserDTO dto = new UserDTO();
        dto.setUsername("a".repeat(256));

        userService.createUser(dto);
    }

    // 异常流程测试 (Error)
    @Test(expected = DuplicateUserException.class)
    public void testCreateUser_duplicateUsername() {
        UserDTO dto = new UserDTO();
        dto.setUsername("duplicate");
        userService.createUser(dto);

        userService.createUser(dto);  // 重复创建
    }
}
```
