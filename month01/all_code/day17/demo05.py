"""
    函数式编程
        将函数赋值给变量
"""


def func01():
    print("func01")


func01()  # 直接调用
# a = func01() # 调用函数,将返回值赋值给变量
a = func01
a()  # 间接调用

def func02():
    print("func02")

def func03(func):
    print("func03")
    # func02() # 直接调用:固定的,不灵活的
    # 确定使用方法(参数与返回值)
    func() # 间接调用:由实参决定搭配关系

func03(func02) #

def func04(p):
    print("参数是:",p)

func03(func04)

