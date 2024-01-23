"""
    局部变量：小范围(一个函数)操作数据
    全局变量：大范围(多个函数)操作数据
"""
# 全局变量：在全局作用域中创建的变量
#           (文件内部)
b = 10


def func01():
    # 局部变量：在局部作用域中创建的变量
    #           (函数内部)
    a = 10
    print(b)  # 在局部作用域中可以读取全局变量


def func02():
    a = 20
    # 没有修改全局变量,而是创建了局部变量
    # b = 20
    # 如果修改全局变量,必须通过global声明
    global b
    b = 20


c = [10]


def func03():
    c[0] = 20  # 修改可变数据,读取全局变量


func03()
print(c)  # [20]