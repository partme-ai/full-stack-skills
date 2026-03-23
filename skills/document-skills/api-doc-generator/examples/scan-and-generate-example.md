# 接口文档生成示例

## 使用场景

当用户需要为项目生成接口文档时，使用此技能。

## 示例对话

### 场景 1: 扫描整个项目生成接口文档

**用户**: "生成接口文档"

**AI 响应**:
1. 扫描项目中的 Controller 类
2. 发现以下 Controller:
   - `com.example.order.OrderController` (5个接口)
   - `com.example.user.UserController` (8个接口)
   - `com.example.product.ProductController` (6个接口)
3. 提取每个接口的详细信息
4. 生成接口文档
5. 保存到 `./docs/api-documentation.md`

### 场景 2: 扫描指定 Controller 生成文档

**用户**: "为 OrderController 生成接口文档"

**AI 响应**:
1. 定位 `OrderController` 类
2. 扫描该 Controller 中的所有接口方法
3. 提取接口信息
4. 生成该模块的接口文档
5. 保存到 `./docs/order-api-documentation.md`

### 场景 3: 扫描多个指定类

**用户**: "扫描 OrderController 和 UserController 生成接口文档"

**AI 响应**:
1. 定位指定的 Controller 类
2. 分别扫描每个 Controller
3. 按模块组织接口
4. 生成完整的接口文档
5. 保存到 `./docs/api-documentation.md`

## 扫描结果示例

### 扫描到的 Controller

```
发现以下 Controller 类：
1. com.example.order.OrderController
   - 接口数量: 5
   - 方法: createOrder, getOrderById, updateOrder, deleteOrder, listOrders

2. com.example.user.UserController
   - 接口数量: 8
   - 方法: createUser, getUserById, updateUser, deleteUser, listUsers, 
          login, logout, changePassword
```

### 生成的文档结构

```markdown
# 订单模块接口文档

## 接口一览表
| 序号 | 接口地址 | 请求方式 | 说明 | 完成情况 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `POST /order` | POST | 创建订单 | ✅ 已完成 |
| 2 | `GET /order/{id}` | GET | 获取订单详情 | ✅ 已完成 |

## 接口定义

### 3.1 创建订单
- **接口地址**: `POST /order`
- **说明**：
  - 该接口对应后端 `OrderController#createOrder`。
  - 用于创建新订单
...
```

## 注意事项

1. 如果项目中没有 Controller 类，会提示用户无法生成文档
2. 如果 Controller 中没有接口方法，会提示用户检查代码
3. 生成的文档会自动保存到 `./docs` 目录
4. 如果 `./docs` 目录不存在，会自动创建
