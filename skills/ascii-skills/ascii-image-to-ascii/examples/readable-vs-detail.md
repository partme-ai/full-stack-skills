# ascii-image-to-ascii：readable vs detail

## Script usage

```bash
python3 scripts/image_to_ascii.py --image ./example.png --width 100 --mode readable
python3 scripts/image_to_ascii.py --image ./example.png --width 100 --mode detail
```

## Output（示意）

readable（轮廓优先）：

```
          ....:::::::....
       ..::---======---::..
     .:--==+++******+++==--:.
    :--=++**##########**++=--:
    :--=++**##########**++=--:
     .:--==+++******+++==--:.
       ..::---======---::..
          ....:::::::....
```

detail（细节优先）：

```
        .:-=+*#%@%#*+=-:.
     .:-=+*#%@@@@@@%#*+=-:.
    .-=+*#%@@@%%%%@@@%#*+=-.
    :=+*#%@@%#*++*#%@@%#*+=:
    .-=+*#%@@@%%%%@@@%#*+=-.
     .:-=+*#%@@@@@@%#*+=-:.
        .:-=+*#%@%#*+=-:.
```

## Notes
- 输出效果强依赖图片预处理：裁剪主体、提升对比度、简化背景
- 如果出现“噪点很多/看不出轮廓”，优先用 readable 或缩小宽度
