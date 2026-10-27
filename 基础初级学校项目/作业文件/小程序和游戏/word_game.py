print("成语接龙游戏")

first = input("你出第一个成语：").strip()
if not first:
    print("成语不能为空。")
else:
    print(f"你的最后一个字是：{first[-1]}")

    second = input(f"请接一个以【{first[-1]}】开头的成语：").strip()
    if not second:
        print("成语不能为空。")
    elif second[0] != first[-1]:
        print("接龙失败：新成语的第一个字不匹配。")
    else:
        print(f"你的最后一个字是：{second[-1]}")

        third = input(f"请接一个以【{second[-1]}】开头的成语：").strip()
        if not third:
            print("成语不能为空。")
        elif third[0] != second[-1]:
            print("接龙失败：新成语的第一个字不匹配。")
        else:
            print(f"接龙成功！你接的是：{third}")
