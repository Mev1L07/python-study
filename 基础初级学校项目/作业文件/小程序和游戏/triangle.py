import math

x1 = float(input("请输入A点x坐标："))
y1 = float(input("请输入A点y坐标："))
x2 = float(input("请输入B点x坐标："))
y2 = float(input("请输入B点y坐标："))
x3 = float(input("请输入C点x坐标："))
y3 = float(input("请输入C点y坐标："))

ab = math.hypot(x2 - x1, y2 - y1)
bc = math.hypot(x3 - x2, y3 - y2)
ac = math.hypot(x3 - x1, y3 - y1)

print(f"AB 边的长度：{ab:.2f}")
print(f"BC 边的长度：{bc:.2f}")
print(f"AC 边的长度：{ac:.2f}")
