while True:
    try:
        code = int(input("输入一个字符编码来查看对应符号（输入 0 退出）："))
    except ValueError:
        print("请输入整数。")
        continue

    if code == 0:
        print("拜拜！")
        break

    if not 0 <= code <= 0x10FFFF or 0xD800 <= code <= 0xDFFF:
        print("编码超出有效范围。")
        continue

    print(chr(code))
