# Core Methodology — Building and Presenting Prompts

## Build the prompt component by component

1. **Subject**: What/who is the main focus? Load `word-library/subject.md` for 人物面部/体型/发型/表情/妆容/年龄/身份 vocabulary. Be specific — "穿墨绿色丝绸旗袍的古典女性" not "一个女人". When describing skin tone, hair color, or clothing color, reach for precise color names from the color references
2. **Scene**: Where is this happening? What time, season, weather? Load `word-library/scene.md` for 场景/环境/天气/时间/地域. If the scene has a strong seasonal feel (spring cherry blossoms, autumn leaves, winter snow), load `gugong-384-colors.md` to find the matching solar-term color palette
3. **Action/Pose**: What is the subject doing? Static or dynamic? Load `word-library/motion.md` for 动作/姿态/互动
4. **Style**: What artistic or photographic style? Load `word-library/style.md` for 风格/艺术运动/摄影技法. This strongly influences the output
5. **Lighting/Color**: What light sources and color palette? **This is where color references become essential**. Load `word-library/lighting.md` for 光线描述; use `color-library.md` for precise hues or `gugong-384-colors.md` for seasonal atmospheric palettes
6. **Composition**: What angle, framing, depth of field? Load `word-library/composition.md` for 构图/视角/镜头
7. **Quality**: Resolution and detail descriptors appropriate to the model version. Load `word-library/quality.md` for 画质/质感

Not every component is needed for every prompt. Use judgment — a minimalist abstract piece may only need subject + style + color. But when color matters, **always consult the color references**; a precisely named color ("胭脂 #9d2933") always outperforms a generic one ("暗红色").

## Present the result

Always present the prompt with:
1. The complete prompt in a code block
2. A brief explanation of key component choices (why this style, why this lighting)
3. Suggested model version and aspect ratio
4. Optional: 1-2 variations with different style/lighting choices
