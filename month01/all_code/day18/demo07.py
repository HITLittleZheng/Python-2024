"""
    闭包
        三大要素
            有外有内
            内使用外
            外返回内
        字面意思
            封闭 外部函数栈帧
        作用:
            外部函数调用后,栈帧保留,供内部函数不断使用
"""


def func01():
    a = 10
    def func02():
        print(a)

    return func02


# 调用外函数,接收内函数
result = func01()
# ...
# 调用内函数
result()
