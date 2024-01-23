"""

"""


# 练习：定义函数,数值累乘
def multiplicative(*args):
    result = 1
    for item in args:
        result *= item
    return result


# 让调用者不必自行构建容器存储多个数据
# 而是由Python解释器自动构建元组包装多个数据
number = multiplicative(42, 54, 56, 65, 76)
print(number)


def multiplicative(args):
    result = 1
    for item in args:
        result *= item
    return result


number = multiplicative([42, 54, 56, 65, 76])
print(number)
