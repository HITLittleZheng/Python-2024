"""
    外部嵌套作用域 ：函数嵌套。
"""

def func01():# 外函数
    a = 10 # 局部变量/外部嵌套变量
    b = 20
    def func02():# 内函数
        # 可以读取外部嵌套变量
        print(a)
        # 如果修改必须先通过nonlocal声明
        nonlocal b
        b = 200

    func02()
    print(b)

func01()