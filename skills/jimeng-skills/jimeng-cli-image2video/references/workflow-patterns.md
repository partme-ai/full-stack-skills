# Workflow Patterns — I2V 执行工作流

> 4 种子命令的标准工作流和错误处理。

---

## 工作流 1：单图生视频

```bash
dreamina user_credit
ls -la ./photo.png                    # 验证图片存在

dreamina image2video \
  --image ./photo.png \
  --prompt="微风吹动发丝，眼睛缓慢眨动，镜头缓缓推近" \
  --duration=6 \
  --poll=60
```

## 工作流 2：首尾帧

```bash
dreamina user_credit
ls -la ./start.png ./end.png          # 验证两张图片

dreamina frames2video \
  --first ./start.png \
  --last ./end.png \
  --prompt="花瓣从含苞到完全盛开，外层先开内层随后逐层绽放" \
  --duration=10 \
  --poll=60
```

## 工作流 3：多帧故事

```bash
dreamina user_credit
# 验证所有帧存在
ls -la ./f1.png ./f2.png ./f3.png ./f4.png

dreamina multiframe2video \
  --images ./f1.png,./f2.png,./f3.png,./f4.png \
  --prompt="沉思→惊喜→急切→喜悦的情绪递进" \
  --transition-prompt="镜头跟随情绪节奏，帧间平滑过渡" \
  --duration=15 \
  --poll=120
```

## 工作流 4：全能参考

```bash
dreamina user_credit
ls -la ./person.png ./scene.png ./music.mp3

dreamina multimodal2video \
  --image ./person.png,./scene.png \
  --audio ./music.mp3 \
  --prompt="图一人物特征配图二场景环境。运动节奏跟随音频。光源统一。色调协调。" \
  --duration=10 \
  --poll=120
```

---

## 文件验证

```bash
# 提交前必须验证所有输入文件存在
ls -la ./input.png

# 多文件逐个验证
for f in ./a.png ./b.png ./c.png; do
  test -f "$f" && echo "OK: $f" || echo "MISSING: $f"
done
```

## 错误处理

| 错误 | 原因 | 解决 |
|------|------|------|
| `AigcComplianceConfirmationRequired` | 模型需首次Web授权 | dreamina网站授权后重试 |
| `Credit insufficient` | 额度不足 | 视频消耗大，告知用户 |
| `file not found` | 图片路径错误 | `ls -la` 验证，使用绝对路径 |
| `invalid sub-command` | 参数名用错 | 检查子命令参数：`--image` vs `--images` vs `--first` |
| `too many images` | 超过限制 | multiframe ≤20, multimodal image ≤9 |
| Poll timeout "querying" | 视频仍在生成 | 非失败。`query_result --submit_id=<id>` |

## 登录排查

```bash
dreamina user_credit                   # 自检
dreamina login --debug                 # 调试
ls -la ~/.dreamina_cli/                # 配置文件
dreamina relogin                       # 切换账号
```
