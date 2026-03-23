# ascii-table-renderer：基础示例

## Input

headers:
- name
- status
- cost

rows:
- ["build", "ok", 12.3]
- ["deploy", "fail", 3.2]
- ["test", "ok", 8.0]

maxWidth: 80
maxColWidth: 20
overflow: ellipsis
borderStyle: light

## Output（readable）

```
+--------+--------+------+
| name   | status | cost |
+--------+--------+------+
| build  | ok     | 12.3 |
| deploy | fail   |  3.2 |
| test   | ok     |  8.0 |
+--------+--------+------+
```

## Script usage

```bash
cat << 'JSON' | python3 scripts/render_table.py --format readable
{
  "headers": ["name", "status", "cost"],
  "rows": [["build","ok",12.3], ["deploy","fail",3.2], ["test","ok",8.0]]
}
JSON
```
