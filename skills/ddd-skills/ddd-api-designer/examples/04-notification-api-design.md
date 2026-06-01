# 通知服务 API 设计案例

> 通知限界上下文（Notification BC）的 REST API 设计，展示消息发送、模板管理等场景。

## 领域模型

```
Notification (Entity)
├── NotificationId
├── UserId
├── Channel: EMAIL / SMS / PUSH
├── TemplateId
├── Status: PENDING / SENT / FAILED
└── SentAt
```

## 端点设计

| 端点 | 类型 | 说明 |
|------|------|------|
| `POST /api/v1/notifications/send` | Command | 发送通知 |
| `POST /api/v1/notifications/batch` | Command | 批量发送 |
| `GET /api/v1/notifications/{id}` | Query | 通知详情 |
| `GET /api/v1/notifications?userId=&status=` | Query | 用户通知列表 |
| `POST /api/v1/notification-templates` | Command | 创建模板 |
| `GET /api/v1/notification-templates` | Query | 模板列表 |
