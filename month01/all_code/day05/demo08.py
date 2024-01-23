"""
    列表推导式
        根据可迭代对象,简单的构建新列表.
        新列表 = [变量 for 变量 in 可迭代对象 if 条件]
"""
# 将列表中大于10的数字存入另外一个列表
list01 = [4, 54, 65, 67, 78, 8, 9]
# new_list = []
# for item in list01:
#     if item > 10:
#         new_list.append(item)
# print(new_list)

new_list = [item for item in list01 if item > 10]
print(new_list)


# 将列表中所有数字的个位存入另外一个列表
new_list = []
for item in list01:
    new_list.append(item % 10)
print(new_list)

new_list = [item % 10 for item in list01]
print(new_list)
