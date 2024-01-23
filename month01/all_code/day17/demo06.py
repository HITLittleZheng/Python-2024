"""
    函数式编程思想:
        适用性:
            多个函数,主体逻辑相同,但核心算法不同.
        步骤:
            1."封装"[分]:根据需求将多个变化点分别定义到函数中
            2."继承"[隔]:将变化的函数抽象为参数
                    在通用函数中先确定参数的使用方式
                    隔离了通用函数与变化函数
            3."多态"[做]:按照通用函数中确定的使用方式,创建变化函数.
"""
list01 = [43, 54, 65, 76, 8, 9]

# 需求:查找第一个小于10的数字
"""
def find_single_lt_10():
    for item in list01:
        if item < 10:
            return item

# 需求:查找第一个大于20的数字
def find_single_gt_20():
    for item in list01:
        if item > 20:
            return item
"""


# 变化
def condition01(item):
    return item < 10


def condition02(item):
    return item > 20


# 不变(通用函数)
def find_single(condition):
    for item in list01:
        # if item < 10:
        # if condition01( item ):
        # if condition02( item ):
        # 统一使用方法
        if condition(item):
            return item

# 新增查找奇数的需求
def condition_new(item):
    return item % 2 != 0


print(find_single(condition_new)) 
print(find_single(condition01))
print(find_single(condition02))
