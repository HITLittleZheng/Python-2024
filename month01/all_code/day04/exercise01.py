"""
# 练习：累加10 -- 60之间，个位不是3/5/8的整数和。
"""
# 思想:满足条件,干
# sum_value = 0
# for number in range(10, 61):
#     unit = number % 10
#     if unit != 3 and unit != 5 and unit != 8:
#         sum_value += number
# print(sum_value)

# 思想:不满足条件,跳
sum_value = 0
for number in range(10, 61):
    unit = number % 10
    if unit == 3 or unit == 5 or unit== 8:
        continue
    sum_value += number
print(sum_value)
