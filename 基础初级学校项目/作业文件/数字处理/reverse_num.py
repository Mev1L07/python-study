number = int(input("请输入一个三位正整数："))

if not 100 <= number <= 999:
    print("输入错误：请输入 100 到 999 之间的整数。")
else:
    hundreds = number // 100
    tens = number // 10 % 10
    ones = number % 10
    reversed_number = ones * 100 + tens * 10 + hundreds

    print(f"倒序后的数字是：{reversed_number}")
