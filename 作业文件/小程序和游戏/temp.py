print("温度转换工具")
print("1. 摄氏度 转 华氏度")
print("2. 华氏度 转 摄氏度")

choice = input("请选择（输入 1 或 2）：")

if choice == "1":
    celsius = float(input("请输入摄氏度："))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius} 摄氏度 = {fahrenheit:.1f} 华氏度")
elif choice == "2":
    fahrenheit = float(input("请输入华氏度："))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} 华氏度 = {celsius:.1f} 摄氏度")
else:
    print("选项无效，请重新运行并输入 1 或 2。")
