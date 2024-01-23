"""
    函数-返回值语法
"""


def func01():
    print("func01执行了")
    return 100  # 返回


data = func01()  # 接收
print(data)
func01()  # 调用者也可以不接受


# Python语言,如果没有返回值,默认返回None
def func02():
    print("func02执行了")
    # return None

func02()
data = func02()
print(data) # None


def func03():
    print("func03执行了")
    return 10 # 结束函数
    print("func03又执行了") # return后面的语句不再执行


data = func03()
print(data) # 10


# break 退出当前循环
# while True:
#     while True:
#         while True:
#             break # 只退出第三层循环
#         break# 只退出第二层循环
#     break# 只退出第一层循环

# return 退出函数(无视循环)
def func04():
    while True:
        while True:
            while True:
                return
