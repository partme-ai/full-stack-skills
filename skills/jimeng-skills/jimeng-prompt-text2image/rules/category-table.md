# 场景分类表

From the user's request, determine the primary category:

| Category | Key Signals | Example File |
|----------|-------------|--------------|
| 人像摄影 | 人物, 肖像, 表情, 自拍, 写真, 证件照 | `examples/portrait.md` |
| 时尚/服装 | 穿搭, 时装, 走秀, 配饰, 珠宝, 包包, 鞋 | `examples/fashion.md` |
| 婚礼/庆典 | 婚礼, 婚纱, 婚庆, 求婚, 纪念日, 派对 | `examples/wedding.md` |
| 儿童/亲子 | 儿童, 宝宝, 亲子, 孕妇, 家庭, 童年 | `examples/children.md` |
| 宠物 | 猫, 狗, 猫狗品种, 萌宠, 宠物日常, 异宠 | `examples/pet.md` |
| 野生动物 | 猛兽, 鸟类, 海洋生物, 昆虫, 两栖, 生态 | `examples/animal.md` |
| 植物/花卉 | 花卉, 绿植, 多肉, 盆景, 园艺, 森林, 微距植物 | `examples/botanical.md` |
| 风景/自然 | 山水, 草原, 沙漠, 雪山, 海洋, 峡谷, 极光 | `examples/landscape.md` |
| 城市/街拍 | 街拍, 都市, 建筑, 纪实, 夜城, 老城 | `examples/street.md` |
| 夜景/暗光 | 夜景, 霓虹, 星空, 烟花, 灯光, 长曝光 | `examples/night.md` |
| 航拍/空中 | 航拍, 鸟瞰, 无人机, 高空, 云端 | `examples/aerial.md` |
| 水下/海洋 | 水下, 潜水, 海洋, 珊瑚, 沉船, 深海 | `examples/underwater.md` |
| 旅行/探险 | 旅行, 探险, 背包客, 公路旅行, 极地, 徒步 | `examples/travel.md` |
| 建筑/室内 | 建筑, 室内设计, 教堂, 极简, 侘寂, 装修 | `examples/architecture.md` |
| 国风/传统 | 汉服, 水墨, 敦煌, 古风, 禅意, 工笔, 戏曲 | `examples/guofeng.md` |
| 二次元/动漫 | 动漫, 二次元, 赛璐珞, 新海诚, 吉卜力, 漫画 | `examples/anime.md` |
| 游戏/电竞 | 游戏, 电竞, 3A大作, 像素, 角色, 装备, 对战 | `examples/game.md` |
| 奇幻/魔幻 | 魔法, 龙, 精灵, 异世界, 城堡, 神话, 剑与魔法 | `examples/fantasy.md` |
| 科幻/未来 | 科幻, 太空, 外星, 机器人, AI, 赛博朋克, 废土 | `examples/scifi.md` |
| 蒸汽朋克 | 蒸汽朋克, 齿轮, 维多利亚, 飞艇, 铜管, 机械 | `examples/steampunk.md` |
| 超现实主义 | 超现实, 梦境, 达利, 马格利特, 荒诞, 错位 | `examples/surreal.md` |
| 极简主义 | 极简, 负空间, 纯色, 几何, 少即是多 | `examples/minimalism.md` |
| 怀旧/复古 | 怀旧, 复古, 胶片, 老照片, 80年代, 民国, 昭和 | `examples/vintage.md` |
| 电影感/氛围 | 电影感, 情绪, 故事感, 王家卫, 雨夜, 文艺 | `examples/cinematic.md` |
| 音乐/舞蹈 | 音乐, 乐器, 舞蹈, 芭蕾, 演唱会, 街舞, 戏曲 | `examples/music-dance.md` |
| 运动/健身 | 运动, 健身, 篮球, 足球, 跑步, 瑜伽, 极限运动 | `examples/sport.md` |
| 交通工具 | 汽车, 摩托车, 飞机, 游艇, 自行车, 火车, 超跑 | `examples/vehicle.md` |
| 美食/饮品 | 美食, 菜品, 甜点, 咖啡, 调酒, 烘焙, 摆盘 | `examples/food-product.md` |
| 科技/数码 | 科技, 数码, 手机, 电脑, 芯片, AI硬件, 3D打印 | `examples/tech.md` |
| 医学/健康 | 医学, 解剖, 手术, 中药, 心理健康, 健身解剖 | `examples/medical.md` |
| 教育/校园 | 学校, 教室, 图书馆, 毕业, 学习, 科学实验 | `examples/education.md` |
| 节日/节庆 | 春节, 中秋, 圣诞, 万圣, 元旦, 国庆, 元宵 | `examples/festival.md` |
| 微距/特写 | 微距, 特写, 昆虫, 水珠, 纹理, 花粉, 雪花 | `examples/macro.md` |
| 抽象/概念 | 抽象, 概念艺术, 几何, 数据可视化, 情感视觉化 | `examples/abstract.md` |
| 商业/营销 | 广告, 海报, 电商, banner, 品牌, 促销, 包装 | `examples/commercial.md` |

If the user's request spans multiple categories, pick the dominant one and borrow elements from others as needed. If no category matches, use the general methodology — the prompt formula works universally.

**After identifying the category**, load the corresponding example file from `examples/` to understand:
- Common scenario patterns within that category
- Category-specific vocabulary and techniques
- Annotated examples showing the methodology applied
