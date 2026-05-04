# Multi-Frame Story — 多帧故事执行

## Examples

### 产品使用演示（4帧）

```bash
dreamina user_credit
ls -la ./step1.png ./step2.png ./step3.png ./step4.png

dreamina multiframe2video \
  --images ./step1.png,./step2.png,./step3.png,./step4.png \
  --prompt="取出产品→在手背涂抹→推开吸收→展现光泽效果。每步是前一步的自然延续。" \
  --transition-prompt="镜头跟随手部动作平滑过渡，每步停留约3秒供观看者理解" \
  --duration=12 \
  --poll=120
```

### 品牌故事（6帧）

```bash
dreamina user_credit
ls -la ./f1.png ./f2.png ./f3.png ./f4.png ./f5.png ./f6.png

dreamina multiframe2video \
  --images ./f1.png,./f2.png,./f3.png,./f4.png,./f5.png,./f6.png \
  --prompt="黎明空城→早高峰人流→午后咖啡馆→黄昏天际线→夜晚霓虹→深夜寂静。城市完整一天的时间流逝。" \
  --transition-prompt="以缓慢节奏横摇串联各场景。早晨场景舒缓，正午略快，夜晚放慢。" \
  --duration=15 \
  --poll=120
```

### 短剧故事板（8帧）

```bash
dreamina user_credit
# 验证8帧
for i in 1 2 3 4 5 6 7 8; do test -f ./story_$i.png && echo "OK: story_$i.png"; done

dreamina multiframe2video \
  --images ./story_1.png,./story_2.png,./story_3.png,./story_4.png,./story_5.png,./story_6.png,./story_7.png,./story_8.png \
  --prompt="女主窗边沉思→收到信息惊喜→匆忙换装→奔跑出门→街头寻找→看到对方→相视而笑。情绪从沉思到喜悦。" \
  --transition-prompt="镜头跟随女主情绪节奏。沉思时缓慢推进，奔跑时快速跟拍，相遇时缓缓推近笑容。" \
  --duration=15 \
  --model_version=seedance2.0 \
  --poll=180
```
