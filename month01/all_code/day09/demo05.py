"""
    函数参数
        实际参数
            1.位置实参
            2.关键字实参
            3.序列实参
            4.字典实参
        形式参数
            5.位置形参
            6.默认形参
            7.星号元组形参
            8.双星号字典形参
            9.命名关键字形参
"""


# 命名关键字形参：要求实参必须是关键字实参
def func01(*args, p):
    print(args)
    print(p)


# 命名关键字形参+默认形参
def func02(*args, p=0):
    print(args)
    print(p)


def func03(p1, *, p2=0):
    print(p1)
    print(p2)


func01(10, 20, p=30)
func02(10, 20)
func02(10, 20, p=30)
func03("a", p2=10)

name = "悟空"
age = 18
# 可以同时打印多个数据
print("我是:", name, ",今年", age, "岁了")
print("我是:", name, ",今年", age, "岁了",sep = "")
print("*",end = " ")
