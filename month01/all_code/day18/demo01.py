"""
    lambda 匿名方法
        语法:
            lambda 参数:函数体
        lambda能完成的功能,def都能完成
        但是lambda函数体只能有一条语句且不能是赋值语句
"""

# def func01(p1, p2):
#     return p1 > p2
#
# print(func01(10, 20)) # ?

# 1. 有参数有返回值
func01 = lambda p1, p2: p1 > p2

print(func01(10, 20))  # ?

# 2. 有参数无返回值
# def func02(p1):
#     print("参数是:",p1)
#
# func02(10)

func02 = lambda p1: print("参数是:", p1)
func02(10)

# 3. 无参数有返回值
# def func03():
#     return 100
#
# print(func03())

func03 = lambda: 100
print(func03())

# 4. 无参数无返回值
# def func04():
#     print("func04")
#
# func04()


func04 = lambda: print("func04")

func04()


# 注意1:lambda函数体只能有一条语句
def func05():
    for i in range(5):
        print(i)


func05()


# func05 = lambda :for i in range(5):print(i)

# 注意2:lambda不支持赋值语句
def func06(p):
    p[0] = 100

list01 = [10]
func06(list01)
print(list01)  # ?

# func06 = lambda p:  p[0] = 100
