# Video Validation Checklist

## 基础校验（必须全部通过）
- [ ] Motion is explicit and specific (concrete action verb, not "有动作")
- [ ] Camera movement clearly described (1-2 movements, Chinese terms)
- [ ] Action complexity matches suggested duration
- [ ] Only one primary subject performing one primary action
- [ ] Light/atmosphere includes temporal change where appropriate
- [ ] Model variant + duration recommendation included

## 进阶校验（方案输出前必查）
- [ ] Prompt style matches recommended model's strength (Rule 8)
      — 长描述散文 → 视频3.0 Pro；结构化短句 → Seedance 2.0
- [ ] Action layer count within model tolerance (Rule 10)
      — Seedance 2.0 ≤ 3 layers; 视频3.0 Pro ≤ 5 layers
- [ ] Light description contains a temporal verb (Rule 5)
      — "洒入"❌ → "缓缓流动""逐渐变亮"✅
- [ ] No hex color codes — Chinese color names only
- [ ] Duration fits action complexity (Rule 4)

## 多方案区分度校验（输出 ≥ 2 方案时）
- [ ] At least 2 dimensions differ between schemes (Rule 9):
      — 运镜 / 动作密度 / 景别 / 节奏 / 场景视角
- [ ] Each scheme has a distinct one-sentence "看片体验" tagline
      — e.g. "情感聚焦型" vs "氛围沉浸型" vs "情绪释放型"
- [ ] No two schemes would look similar in actual output
