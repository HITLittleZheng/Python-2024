"""
    继承 - 数据
"""




"""
# 若子类没有构造函数,直接使用父类的构造函数
class Student(Person):
    pass
 
zs = Student("张三")
print(zs.name)
"""

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

# 若子类有构造函数,覆盖父类构造函数(好像他不存在)
# 此时必须通过super函数调用父类构造函数
class Student(Person):
    # 子类构造函数参数:父类参数+子类参数
    def __init__(self, name="", age=0, score=0):
        super().__init__(name, age)
        self.score = score


# 创建子类对象,执行子类构造函数
zs = Student("张三", 26, 100)
print(zs.__dict__)
