score = float(input("请输入你的 Python 考试成绩（0 到 100）："))

if not 0 <= score <= 100:
    print("成绩应在 0 到 100 之间。")
elif score >= 85:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格，继续努力。")
