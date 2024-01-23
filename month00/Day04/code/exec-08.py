"""
    循环 打印 1-10之间的奇数

    计算20以内不能被2 5 整数的数之和
"""

# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue
#     print(num)

# for item in range(1, 11):
#     if item % 2:
#         print(item)

# for item in range(1, 11, 2):
#     print(item)


sums = 0
for i in range(20):
    if not i % 2 or not i % 5:
        continue
    # print(i)
    sums += i

print('最终的和为：', sums)
