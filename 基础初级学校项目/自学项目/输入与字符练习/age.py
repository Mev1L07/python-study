name = input("请问你叫什么？").strip()
age = int(input("你几岁？"))

if age < 0:
    print("年龄不能是负数。")
else:
    print(f"Hello, {name}！")
    print(f"你今年 {age} 岁，再过 10 年就 {age + 10} 岁了。")
