"""
    封装行为
        私有成员
            目的:让类成员不被类外访问(隐藏)
            语法:命名以双下划线开头
            本质:障眼法
                看上去是双下划线的私有变量名
                    例如:__data
                实际上是单下划线+类名+私有变量名
                    例如:_MyClass__data
"""


class MyClass:
    def __init__(self, data=0):
        self.__data = data

    def __func01(self):
        print(self.__data)

    # 公开成员内部可以访问私有成员
    def func02(self):
        print("func02执行了")
        self.__func01()
        print(self.__data)

m = MyClass(10)
# print(m._MyClass__data) # 不建议
# print(m.__data)
# m.__func01()
m.func02() # 调用公开的方法(内部访问私有成员)

print(m.__dict__)
