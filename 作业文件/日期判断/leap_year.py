print("=" * 35)
print(" 🗓️  欢迎使用闰年查询小助手")
print("=" * 35)

while True:
    year_input = input("\n请输入一个年份（输入 q 退出）：").strip()

    if year_input.lower() == "q":
        print("👋 拜拜！下次有需要再来找我。")
        break

    if not year_input.isdigit():
        print("⚠️ 格式错误：请输入纯数字的年份哦！")
        continue

    year = int(year_input)
    if year == 0:
        print("⚠️ 年份必须大于 0。")
        continue

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"✅ 结果：{year} 年是【闰年】！这一年有 366 天。")
    else:
        print(f"❌ 结果：{year} 年不是闰年。这一年只有 365 天。")
