# Video-Specific Writing Rules

### Rule 1: Motion is mandatory and explicit

- ✗ "一个女孩在森林里" → ✓ "一个女孩在森林里缓缓行走，裙摆随步伐摆动，阳光透过树叶在她身上流动"

### Rule 2: Camera movement tells the story

- **Push in (推)**: focus, intensity, revelation
- **Pull out (拉)**: context, isolation, ending
- **Pan (摇)**: exploration, connection, following
- **Track (移)**: immersion, journey, discovery

### Rule 3: One clear action per clip

Seedance 2.0 works best with a single clear action. For 15s clips, 2-3 stage progression OK but keep each stage simple.

### Rule 4: Duration determines action complexity

| Duration | Action Complexity |
|----------|------------------|
| 4-6s | One clear action ("转身微笑") |
| 7-10s | Action with development ("从远处走来→经过镜头→渐行渐远") |
| 11-15s | 2-3 stage progression ("推门→环顾→走向窗边") |

### Rule 5: Light can (and should) change — with temporal language

Describe how light **transforms over time** — not just its starting state.

✅ "晨光透过薄纱窗帘逐渐变亮，光影在母亲面庞上缓缓移动"
✅ "夕阳缓缓沉入海平面，光线从金黄渐变为橘红"
✅ "霓虹灯渐次亮起，招牌的蓝光在水洼中跳动"
✅ "烛光在微风中摇曳，阴影在墙壁上轻轻舞动"
✗ "清晨的柔和光线透过窗帘洒入"（静态描述 → 缺少变化感）
✗ "暖色台灯散发着柔和的光晕"（静态 → 光没有在变）

**Temporal light vocabulary:**
`光线逐渐变亮` · `光线渐暗` · `光影流动` · `光斑在地面缓缓移动` · `阴影拉长` · `晨光渐浓` · `暮色渐沉` · `烛光摇曳` · `灯光渐次亮起` · `阳光角度缓慢偏移` · `穿透云层的光束缓慢移动` · `水面反光跳动闪烁`

**Rule of thumb**: If you can replace the light description with a photo caption, it's static. A video light description should contain a verb that implies time. "洒入" is still a snapshot — "缓缓流动""逐渐变亮" carries the time dimension.

### Rule 6: Camera in the latter half

Subject + action + scene → camera work → atmosphere → style

### Rule 7: Official guide (视频3.0 Pro) — 8 control dimensions

When using 视频3.0/3.0 Pro, leverage these 8 dimensions from `references/jimeng-video-3.0-guide.md`:

1. **动作指令** — 单一动作(简单) / 时序组合动作(复杂)
2. **情绪演绎** — 赋予场景情感基调
3. **场景描述** — 明确的时间/地点/天气
4. **风格描述** — 风格直出(T2V) / 风格延续(I+T2V/I2V)
5. **镜头语言** — 基础运镜+进阶运镜+景别视角控制
6. **Prompt控制美感** — 人物外形+画面美感
7. **切镜能力** — 镜头切换和转场
8. **创意特效** — 首尾帧类型/玩法/I+T2V特效

---

### Rule 8: Match prompt style to model version — 致命误区

Each model excels at different writing styles. **Mismatching will degrade output quality severely.**

| Prompt 风格特征 | 推荐模型 | 原因 |
|---|---|---|
| 大段自然语言、细腻场景铺陈、氛围描写、多感官描述 | **视频3.0 / 3.0 Pro** | 官方公式 = 自然语言自由书写。长文本理解力强，善于从散文中提炼场景要素 |
| 结构化短句、分段清晰、动词集中、运镜指令明确 | **Seedance 2.0 系列** | 官方公式 = 分解式 `主体 + 动作/运动 + 空间背景/光影/风格 + 镜头调度/音效`。对结构化指令的解析更准 |
| 极简动作 + 氛围主导 | **视频3.0 Pro** | 氛围理解力强，能补充细节 |
| 需要抽帧/慢动作/首尾帧特效 | **视频3.0 Pro** | 支持创意特效维度 |
| 需要原生音频/多模态参考 | **Seedance 2.0** | 原生音视频联合生成 |
| 图生视频 | **Seedance 2.0** (I2V/V2V) 或 **视频3.0 Pro** (I+T2V) | 根据是否需要图像外的控制力选择 |

**Wrong assignment example（来自实际案例）**:
- ❌ 长描述自然语言 prompt → 推荐 Seedance 2.0 → Seedance 对散文式描述的语义解析不如 3.0 Pro，细节易丢失
- ✅ 长描述自然语言 prompt → 推荐 视频3.0 Pro → 发挥其自然语言理解优势
- ✅ 如果坚持用 Seedance 2.0 → 将长描述重写为结构化短句版本

**Rule of thumb**:
> 如果你的 prompt 是一段散文 → 选 **视频3.0 Pro**
> 如果你的 prompt 是分段清单 → 选 **Seedance 2.0**
> 如果你的 prompt 两者都可以 → **推荐优先视频3.0 Pro**（容错率更高）

### Rule 9: Multi-scheme differentiation — 方案区分度

When providing multiple alternatives for the same scene, ensure each scheme delivers a **visually distinct** viewing experience. Similar schemes waste the user's choice.

✅ **Good differentiation:**
- 方案A: 慢镜头推近 + 手部微动作 → 情感聚焦型
- 方案B: 固定镜头 + 环境呼吸感（窗帘飘动/光影流动）→ 氛围沉浸型
- 方案C: 亲吻 + 抬头 + 全景 → 情绪释放型

❌ **Bad differentiation (real example):**
- 方案A: 慢镜头 + 推近 + 抚摸 + 花瓣颤动 → 温情
- 方案B: 慢镜头 + 极缓推近 + 窗帘飘动 + 呼吸 → 氛围
→ 两者核心视觉差异不显著，实际成片难区分

**Differentiation checklist for each new scheme:**
1. ❓ 运镜方案不同？（推 vs 固定 vs 环绕 vs 摇）
2. ❓ 动作/情绪密度不同？（高能量 vs 低能量）
3. ❓ 景别/构图不同？（特写 vs 中景 vs 全景）
4. ❓ 节奏/时长不同？（5s 紧凑 vs 10s 舒展）
5. ❓ 场景/视角不同？（室内 vs 室外？主观 vs 客观？）
6. ❓ 如果以上 5 条都相似 → **合并 or 重新构思** — 用户不需要两个同质的选项

**At minimum, differentiate on 2+ dimensions.**

### Rule 10: Action layer count — by model tolerance

Different models have different tolerance for multi-layer motion.

| Layer Count | Definition | 视频3.0 Pro | Seedance 2.0 |
|---|---|---|---|
| **1 layer** | 一个主要动作（如"一个人行走"） | ✅ 安全 | ✅ 安全 |
| **2-3 layers** | 主体动作 + 1-2 环境/自然动态（如"行走+树叶飘落"） | ✅ 安全 | ✅ 安全 |
| **4-5 layers** | 主体动作 + 微表情 + 环境动态 + 次对象动作（如"抚摸+微笑+发丝+花瓣+手指颤动"） | ✅ 可行 | ⚠️ risk — 可能出现部分动态丢失或 artifacts |
| **6+ layers** | 多主体交互 + 多层环境动态 | ⚠️ risk | ❌ 不建议 — distortion 风险高 |

**Rule**: For Seedance 2.0, cap action layers at 3 (one primary + up to 2 secondary/environmental). For 视频3.0 Pro, 4-5 layers is acceptable — use the 5th layer for micro-expressions or subtle environmental detail.
