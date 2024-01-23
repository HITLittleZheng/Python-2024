"""
    将 1 - 20 之间的整数, 每五个数是一行进行打印
"""

i = 0
while i < 20:
    i += 1
    print(i, end=" ")
    if i % 5 == 0:
        print()
