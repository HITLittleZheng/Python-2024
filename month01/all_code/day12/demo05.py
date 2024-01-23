"""
    属性-原理
        目的:保护类中数据,在有效范围内.
"""

class Wife:
    def __init__(self, name="", age=0):# 2
        self.name = name
        # self.__age = age
        self.set_age(age)
    # 修改
    def set_age(self, value):# 3
        if value > 30:
            value = 30
        elif value < 20:
            value = 20
        # 私有的实例变量
        self.__age = value
    # 读取
    def get_age(self):
        return self.__age
a_ke = Wife("阿珂", 100) # 1
# a_ke.age = 200
a_ke.set_age(200)
print(a_ke.name)
# print(a_ke.age)
print(a_ke.get_age())
