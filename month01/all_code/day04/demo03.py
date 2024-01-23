"""
    跳转语句
"""
# 需求:累加1--100之间所有整数
# 条件:数字能被3整除
# 思想:满足条件执行
# sum_value = 0
# for number in range(1, 101):
#     if number % 3 == 0:
#     # if not number % 3: # 没值
#         sum_value += number
# print(sum_value)

# 思想:不满足条件跳过,否则执行
sum_value = 0
for number in range(1, 101):  # 一盘瓜子
    if number % 3 != 0:  # 如果遇到坏瓜子
        # if number % 3: # 有值
        continue  # 跳过  # 吐出来
        # break  # 跳出
    sum_value += number
print(sum_value)
