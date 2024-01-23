"""
    定义函数，在列表中查找奇数
    定义函数，在列表中查找能被3或5整除的数字
"""
list01 = [45, 56, 567, 78, 89]


def find_single01():
    for item in list01:
        if item % 2 != 0:
            return item

def find_single02():
    for item in list01:
        if item % 3 == 0 or item % 5 ==0:
            return item

print(find_single01())

# 参数是:列表中的元素
# 返回值:给到if做判断
def condition01(item):# 3
     return item % 2 != 0

def condition02(item):
    return item % 3 == 0 or item % 5 ==0

# 高阶函数:参数是函数的函数
def find_single(condition):# 2
    for item in list01:
        # if item % 3 == 0 or item % 5 ==0:
        # if condition01(item):
        # if condition02(item):
        if condition(item):
            return item

print(find_single(condition01))# 1