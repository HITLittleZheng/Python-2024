"""
    生成 1--10 的整数存入列表！
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    生成 1--10 的整数 将不能被3整除的数存入列表！
        [1, 2, 4, 5, 7, 8, 10]
"""

#  生成 1--10 的整数存入列表！
list_int = []

for i in range(1, 11):
    list_int.append(i)

print(list_int)

# 生成 1--10 的整数 将不能被3整除的数存入列表！
list_num = []
for i in range(1, 11):
    if i % 3 != 0:
        list_num.append(i)

print(list_num)
