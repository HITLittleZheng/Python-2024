"""
    重写:
        语法:子类拥有和父类相同的方法
        目的:子类改变父类的行为
"""


class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 自定义对象 --> 整数
    # def __int__(self):
    #     return self.age

    # 自定义对象 --> 字符串
    def __str__(self):
        return f"{self.name}的年龄是{self.age}"

zs = Person("张三", 26)
# 直接打印自定义对象的格式:
# <__main__.Person object at 0x7f9ccf69fe10>
print(zs) # print(zs.__str__())
# 在print函数内部,调用的是对象的__str__方法

# print(int(zs)) #  print(zs.__int__())

