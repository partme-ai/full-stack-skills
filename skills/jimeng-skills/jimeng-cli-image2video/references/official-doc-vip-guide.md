# 官方文档 VIP 通道指南

来源：即梦 CLI 体验指南（ByteDance 内部飞书文档）
抓取时间：2026-05-14
URL：https://bytedance.larkoffice.com/wiki/FVTwwm0bGiishxkKOoScdHR2nsg

## 官方更新日志中的 VIP 记录

| 版本 | 日期 | 内容 |
|------|------|------|
| v1.3.2 | 2026-04-05 | 新增：支持 seedance2.0fast_vip 以及 seedance2.0_vip 通道提速，畅快生成 |
| v1.4.3 | 2026-05-07 | 新增：支持 seedance 2.0 vip 模型以 1080p 分辨率生视频 |

## image2video 系列 VIP 支持

| 子命令 | 支持的 VIP 模型 | 默认值 | 1080P？ |
|--------|----------------|--------|---------|
| `image2video` | `seedance2.0fast_vip`, `seedance2.0_vip` | `seedance2.0fast_vip` | ✅ 仅 `seedance2.0_vip` |
| `frames2video` | `seedance2.0fast_vip`, `seedance2.0_vip` | `seedance2.0fast_vip` | ✅ 仅 `seedance2.0_vip` |
| `multimodal2video` | `seedance2.0fast_vip`, `seedance2.0_vip` | `seedance2.0fast_vip` | ✅ 仅 `seedance2.0_vip` |
| `multiframe2video` | ❌ 不支持 model_version | — | — |

## 注意事项

- CLI 默认 model_version 是 `seedance2.0fast`（非 VIP），需要显式指定 `_vip` 变体
- 官方文档示例命令均未加 `--model_version`，走默认非 VIP 通道
- 社区确认：需高级会员（VIP）才可使用 VIP 模型版本
- VIP 通道有独立队列，速度更快、并发更高
