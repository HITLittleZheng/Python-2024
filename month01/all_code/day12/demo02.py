"""
    小结-Python语言变量
"""
# 1.全局变量:整个文件可用
data01 = 10


def func01():
    # 2.局部变量:当前函数可用
    data02 = 20


class MyClass:
    # 4.类变量:通过类访问
    data04 = 40

    def __init__(self):
        # 3.实例变量:通过实例访问
        self.data03 = 30

    def func02(self):
        print(self.data03)
        print(MyClass.data04)


m01 = MyClass()
print(m01.data03)
print(MyClass.data04)
