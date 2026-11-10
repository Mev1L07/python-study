age = int(input("请输入你的年龄："))

if age < 0:
    print("年龄不能是负数。")
else:
    if age >= 18:
        print("你已经成年了。")
    else:
        print(f"距离 18 岁还有 {18 - age} 年。")
