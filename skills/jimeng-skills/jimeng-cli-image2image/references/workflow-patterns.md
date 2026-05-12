# Workflow Patterns — I2I 执行工作流与错误处理

> CLI 图生图编辑的标准工作流模式和常见错误处理方案。

---

## 工作流 1：标准 I2I 编辑（最常用）

**场景**: 用户有参考图和写好的编辑提示词

**步骤**:
```bash
# 1. 检查额度
dreamina user_credit

# 2. 验证图片存在
ls -la ./input.png

# 3. 提交编辑
dreamina image2image \
  --images ./input.png \
  --prompt="<edit prompt with Keep/Change>" \
  --model_version=5.0 \
  --resolution_type=4k \
  --poll=30

# 4. 结果自动返回（或 poll 超时后 query_result）
```

---

## 工作流 2：批量 I2I 编辑

**场景**: 对多张图片进行相同的风格转换

**步骤**:
```bash
dreamina user_credit

# 异步批量提交
for img in photo1.png photo2.png photo3.png; do
  dreamina image2image \
    --images ./$img \
    --prompt="保持构图和人物不变，转换成水墨画风格，黑白灰墨色，留白" \
    --poll=0
  # 记录每个 submit_id
done

# 稍后查询
dreamina list_task --gen_status=success
```

---

## 工作流 3：多图参考合成

**场景**: 用2-3张参考图分别提供不同元素

**步骤**:
```bash
dreamina user_credit

# 确认所有参考图存在
ls -la ./subject.png ./style.png ./background.png

# 提交多图合成
dreamina image2image \
  --images ./subject.png,./style.png,./background.png \
  --prompt="参考第一张的人物特征，应用第二张的水墨风格，配上第三张的竹林背景。所有元素光源方向统一。全局色调协调。" \
  --poll=30
```

---

## 工作流 4：与提示词技能协作

**场景**: jimeng-prompt-image2image 写好编辑提示词，用户批准后执行

**步骤**:
```
1. jimeng-prompt-image2image 创建编辑提示词（Keep/Change框架） → 用户批准
2. jimeng-cli-image2image 执行：
   a. dreamina user_credit
   b. ls -la <image paths>           ← 验证图片存在
   c. dreamina image2image --images ... --prompt="<approved>"
   d. 报告结果
```

---

## 错误处理

### 错误：额度不足
```
Error: credit insufficient
```
**响应**: 告知用户余额，建议检查 `dreamina user_credit`。

### 错误：模型需要首次授权
```
Error: AigcComplianceConfirmationRequired
```
**响应**: 引导用户去 dreamina 网页端授权后重试。

### 错误：图片文件不存在
```
Error: file not found / cannot read image
```
**响应**: 
1. 用 `ls -la <path>` 验证文件存在
2. 建议使用绝对路径
3. 检查文件格式（支持 PNG/JPG/JPEG/WEBP）

### 错误：模型版本不支持
```
Error: model version not supported for image2image
```
**响应**: I2I 仅支持 4.0+。检查 `--model_version` 参数。

### 错误：分辨率不支持
```
Error: resolution_type not supported
```
**响应**: I2I 仅支持 2k 和 4k。不支持 1k。

### 错误：图片数量超限
```
Error: too many images
```
**响应**: 最多10张。减少 `--images` 中的文件数量。

### 错误：CLI未安装/未登录
**响应**: 
```bash
curl -fsSL https://jimeng.jianying.com/cli | bash
dreamina login
dreamina login --debug  # 如果浏览器登录卡住
```

### 错误：轮询超时（非真正错误）
```
Status: querying (poll timeout)
```
**响应**: 用 `dreamina query_result --submit_id=<id>` 继续查询。

---

## 图片验证最佳实践

```bash
# 提交前验证
ls -la ./input.png                    # 确认存在
file ./input.png                      # 确认是图片
identify ./input.png 2>/dev/null      # 如果有ImageMagick，查看尺寸

# 多图时逐个验证
for img in a.png b.png c.png; do
  test -f ./$img && echo "OK: $img" || echo "MISSING: $img"
done
```

---

## 登录与配置故障排查

```bash
dreamina user_credit                   # 自检
dreamina login --debug                 # 调试登录
ls -la ~/.dreamina_cli/                # 检查配置
cat ~/.dreamina_cli/config.toml        # 确认内容
dreamina relogin                       # 切换账号
dreamina logout                        # 清除凭证
```
