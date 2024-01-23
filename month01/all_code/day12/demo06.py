"""
    属性property
        本质:建立了实例变量与读写方法的关联关系
            属性内部在检测对变量的读写操作
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # 当存在属性时,本行代码访问的是属性
        self.age = age  # self.set_age(age)

    def set_age(self, value):
        if value > 30:
            value = 30
        elif value < 20:
            value = 20
        self.__age = value

    def get_age(self):
        return self.__age

    age = property(get_age, set_age)


a_ke = Wife("阿珂", 100)
a_ke.age = 200  # a_ke.set_age(200)
print(a_ke.name)
print(a_ke.age)  # a_ke.get_age()
