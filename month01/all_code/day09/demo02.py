"""
    函数参数
        实际参数
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 位置实参：按照顺序与形参对应
func01(1, 2, 3)
# TypeError: func01() missing 1 required positional argument: 'p3'
# func01(1, 2)
# TypeError: func01() takes 3 positional arguments but 4 were given
# func01(1, 2, 3, 4)
# 关键字实参：按照名称与形参对应
func01(p1=1, p3=3, p2=2)
# TypeError: func01() got an unexpected keyword argument 'pp'
# func01(p1 = 1,p3 = 3,pp = 2)
