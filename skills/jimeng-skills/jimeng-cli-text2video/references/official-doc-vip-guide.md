# 官方文档 VIP 通道指南

来源：即梦 CLI 体验指南（ByteDance 内部飞书文档）
抓取时间：2026-05-14
URL：https://bytedance.larkoffice.com/wiki/FVTwwm0bGiishxkKOoScdHR2nsg

## 官方更新日志中的 VIP 记录

| 版本 | 日期 | 内容 |
|------|------|------|
| v1.3.2 | 2026-04-05 | 新增：支持 seedance2.0fast_vip 以及 seedance2.0_vip 通道提速，畅快生成 |
| v1.4.3 | 2026-05-07 | 新增：支持 seedance 2.0 vip 模型以 1080p 分辨率生视频 |

## CLI 支持的 VIP 模型版本（所有视频子命令）

| 子命令 | VIP 模型版本 | 非 VIP 版本 |
|--------|-------------|------------|
| `text2video` | `seedance2.0fast_vip`, `seedance2.0_vip` | `seedance2.0fast`, `seedance2.0` |
| `image2video` | `seedance2.0fast_vip`, `seedance2.0_vip` | 同上 + 3.0/3.0fast/3.0pro/3.5pro |
| `frames2video` | `seedance2.0fast_vip`, `seedance2.0_vip` | 同上 + 3.0/3.5pro |
| `multimodal2video` | `seedance2.0fast_vip`, `seedance2.0_vip` | `seedance2.0fast`, `seedance2.0` |
| `multiframe2video` | ❌ 不支持 model_version 参数 | — |

## VIP 额外能力

`seedance2.0_vip` 支持 **1080P** 分辨率（普通版仅 720P）。

## 注意事项

- CLI 默认的 model_version 是 `seedance2.0fast`（非 VIP），需要**显式指定** `_vip` 变体
- 官方文档的示例命令全部**没有**加 `--model_version` 参数，走的是默认非 VIP 通道
- 社区用户确认：需高级会员（VIP）才可使用 VIP 模型版本
- 官方维护者 user 2448 回复："使用时指定 --model_version 参数为 seedance2.0_vip, 或 seedance2.0fast_vip 即可"

## 验证方法

```bash
# 查看 CLI 实际支持的 model_version 列表（官方指引）
dreamina text2video -h        # 查看 text2video 支持的模型
dreamina image2video -h       # 查看 image2video 支持的模型
```
