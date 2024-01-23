"""
    装饰器 - 标准
        内函数的返回值:旧功能的返回值
"""

def func_new(func):
    def wrapper(*args):# 2            合
        print("新功能")
        res = func(*args) # 调用旧功能  拆
        return res
    return wrapper

# func01 = func_new(func01)
@func_new
def func01(p1):# 3
    print("旧功能1")
    return 100

@func_new
def func02(p1,p2):# 3
    print("旧功能2")

# func01 = func_new(func01)
# func02 = func_new(func02)

# 1
value = func01(10) # 调用内函数
value = func02(10,20) # 调用内函数
print(value)
