# Video Core Methodology — Building and Presenting

## Build the prompt component by component

1. **Subject** (主体): What/who is the main focus? Be specific
2. **Action/Motion** (动作/运动): **THE critical video component**. Describe what moves, how, at what speed. Use motion vocabulary from `word-library.md`. Be explicit — "缓缓转身，长发随风飘动" not "动了一下"
3. **Scene** (场景): Where + when. Provides context for the motion
4. **Camera Movement** (运镜): How the camera moves. Use `camera-library.md`. Pick 1-2 movements max
5. **Lighting/Atmosphere** (光影氛围): In video, describe **how light changes** over time — flickering, shifting, dimming. NOT just its starting state. Use temporal verbs (参考 Rule 5 和 temporal light vocabulary).
6. **Duration/Pacing** (时长/节奏): How long + how fast. Seedance 2.0 supports 4-15 seconds
7. **Style/Quality** (风格/画质): Video-specific quality terms like "电影级画质""高帧率流畅""4K视频"

### CRITICAL: Choose model BEFORE writing

The writing style must match the target model (Rule 8). Decide your model first, then write the prompt in that model's native language.

| If target model is | Write in this style |
|---|---|
| **视频3.0 / 3.0 Pro** | Natural language prose — descriptive paragraphs, sensory detail, soft scene setting. The model extracts structure from free text. |
| **Seedance 2.0** | Structured segments — clear subject→action→scene→camera breakdown. Use shorter sentences, explicit camera directions, separate motion from atmosphere. |

**Before building, first decide which model, then load the corresponding guide.**

**At each component step**, also apply these rules:
- Motion first, scene second — place action description before or immediately after the subject
- One primary movement — complex multi-subject interactions + camera work tend to fail
- Chinese camera terms > English — "镜头缓缓推进" > "dolly in slowly"
- Match action to duration — 5s = one clear action; 10s = action with development; 15s = multi-stage progression
- Describe how light changes — unlike images, video light can evolve: "夕阳逐渐西沉""烛光摇曳闪烁"
- Action layer count — Seedance 2.0 ≤ 3 layers; 视频3.0 Pro ≤ 5 layers (参考 Rule 10)

## Present the result

Always present: complete prompt in code block + model variant + suggested duration + camera explanation + optional variations.

### Multi-scheme outputs (≥ 2 alternatives)

When presenting multiple schemes, verify differentiation (Rule 9) and include a **one-line "看片体验" tagline** for each:
- ✅ "情感聚焦型 — 推镜逼近母子互动，突出情绪细节"
- ✅ "氛围沉浸型 — 固定镜头搭配环境呼吸感，宁静治愈"
- ✅ "情绪释放型 — 亲吻+抬头+微笑，5秒短而有力"
