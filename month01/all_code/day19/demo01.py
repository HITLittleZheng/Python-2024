"""
    装饰器 - 推导过程
        在不改变旧功能调用与定义的情况下,
        为其增加新功能

        闭包三大要素在装饰器中的作用:
            有外有内:外在接收旧功能,内函数包装新旧功能
            内访问外:希望同时执行新旧功能
            外返回内:日后根据需求执行新旧功能
"""

"""
def func01():
    print("旧功能")


def func_new():
    print("新功能")

# 新功能完全覆盖了旧功能
# func01 = func_new
 
func01()
"""

"""
def func01():
    print("旧功能")


def func_new(func):
    print("新功能")
    func()
 
# 并不希望在本行执行新旧功能
func01 = func_new(func01)

func01()
# ....
func01()
"""


def func01():
    print("旧功能")


def func_new(func):
    def wrapper():
        print("新功能")
        func()
    return wrapper  # 返回内函数

# 调用外函数(不执行内函数)
func01 = func_new(func01)
# 调用内函数
func01()
# ....
func01()
