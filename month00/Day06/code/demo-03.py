"""
    列表推导式
        用 可迭代对象 快速生成列表
        语法：
            [ 表达式 for 变量 in 可迭代对象]
            [ 表达式 for 变量 in 可迭代对象 if 条件表达式]
"""
#  生成 1--10 的整数存入列表！
# list_int = []
#
# for i in range(1, 11):
#     list_int.append(i)

list_int = [i for i in range(1, 11)]
print(list_int)

# 生成 1--10 的整数 将不能被3整除的数存入列表！
# list_num = []
# for i in range(1, 11):
#     if i % 3 != 0:
#         list_num.append(i)

list_num = [i for i in range(1, 11) if i % 3 != 0]
print(list_num)

# 生成 1--10 的整数 将不能被3整除的平方存入列表！
list_num = [i ** 2 for i in range(1, 11) if i % 3 != 0]
print(list_num)
