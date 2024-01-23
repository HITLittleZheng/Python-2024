"""
    属性-标准
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    @property  # age = property(age)
    def age(self):  # 负责读数据
        return self.__age

    @age.setter  # age = age.setter( age  )
    def age(self, value):
        if value > 30:
            value = 30
        elif value < 20:
            value = 20
        self.__age = value


a_ke = Wife("阿珂", 100)
a_ke.age = 200  # a_ke.set_age(200)
print(a_ke.name)
print(a_ke.age)  # a_ke.get_age()
