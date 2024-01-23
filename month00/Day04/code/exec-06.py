"""
    打印 10-20 的数字  个位 非 3 5 7 的数.
"""

num = 9
while num <= 20:
    num += 1
    ge_number = num % 10

    if ge_number == 3 or ge_number == 5 or ge_number == 7:
        continue

    print(num)
