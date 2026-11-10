number = int(input("请输入一个非负整数："))

if number < 0:
    print("输入错误：阶乘不能用于负数。")
else:
    result = 1
    current = 1
    while current <= number:
        result *= current
        current += 1

    print(f"{number}! = {result}")
