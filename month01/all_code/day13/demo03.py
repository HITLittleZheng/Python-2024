"""
    继承
        财产:钱不用儿子挣,但是可以直接花
        编程:代码不用子类写,但是可以直接用
"""
# 适用性:多个类型,代码上有共性且概念上统一("都是一种")

"""
class Student:
    def play(self):
        print("在玩耍")
    
    def say(self):
        print("在讲话")

class Teacher:
    def teach(self):
        print("在教学")
    
    def say(self):
        print("在讲话")
"""


# 父类:体现共性
class Person(object):
    def say(self):
        print("在讲话")


# 子类:体现个性
class Student(Person):
    def play(self):
        print("在玩耍")
        self.say()  # 类中通过self调用父类方法


class Teacher(Person):
    def teach(self):
        print("在教学")


# 子类对象既能访问自身也能访问父类成员
qtx = Teacher()
qtx.teach()
qtx.say()  # 类外通过对象名调用父类方法

# 父类对象只能访问自身成员
zs = Person()
zs.say()

# 关系判定
# 老师对象 是一种 人类型
print(isinstance(qtx, Person))  # True
# 人对象 是一种 人类型
print(isinstance(zs, Person))  # True
# 人对象 是一种 老师类型
print(isinstance(zs, Student))  # False

# 老师类型 是一种 人类型
print(issubclass(Teacher, Person))  # True
# 人类型 是一种 人类型
print(issubclass(Person, Person))  # True
# 人类型 是一种 老师类型
print(issubclass(Person, Student))  # False

# 老师对象的类型 是 人类型
print(type(qtx) == Person)  # False
# 人对象的类型 是 人类型
print(type(zs) == Person)  # True
# 人对象的类型 是 人类型
print(type(zs) ==  Student)  # False