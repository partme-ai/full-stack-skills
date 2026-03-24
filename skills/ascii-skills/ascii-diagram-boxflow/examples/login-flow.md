# ascii-diagram-boxflow：登录流程（TB）示例

## Input

nodes:
- Start
- Input
- Validate
- Success
- Fail

edges:
- Start -> Input
- Input -> Validate
- Validate -> Success
- Validate -> Fail

## Output（示意，ASCII-only）

```
+--------------+
|    Start     |
+--------------+
       |
       v
+--------------+
|    Input     |
+--------------+
       |
       v
+--------------+
|   Validate   |
+--------------+
    |     |
    v     v
+--------+  +--------+
|Success |  |  Fail  |
+--------+  +--------+
```

## Script usage（线性/简单分支 best-effort）

```bash
cat << 'JSON' | python3 scripts/boxflow.py
{
  "nodes": ["Start", "Input", "Validate", "Success", "Fail"],
  "edges": [["Start","Input"], ["Input","Validate"], ["Validate","Success"], ["Validate","Fail"]]
}
JSON
```
