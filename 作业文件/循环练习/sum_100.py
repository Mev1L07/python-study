odd_total = 0
number = 1
while number <= 100:
    odd_total += number
    number += 2

even_total = 0
number = 2
while number <= 100:
    even_total += number
    number += 2

all_total = 0
number = 1
while number <= 100:
    all_total += number
    number += 1

print(f"1 到 100 的奇数和：{odd_total}")
print(f"1 到 100 的偶数和：{even_total}")
print(f"1 到 100 的总和：{all_total}")
