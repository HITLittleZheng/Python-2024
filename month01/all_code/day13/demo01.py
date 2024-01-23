"""
    复习-属性
         作用:保护数据有效性
    属性各种写法
        读写属性
        只读属性
        只写属性(仅供了解)
"""


# 写法1:读写属性
#       在实例变量读写过程中进行控制(数据验证,修改)
# 快捷键:props + 回车
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value

shuang_er = Wife("双儿", 28)
print(shuang_er.__dict__)
print(shuang_er.name)
print(shuang_er.age)


# 写法2:只读属性
#        为私有变量提供读取功能
# 快捷键:prop + 回车
class Wife:
    def __init__(self, name=""):
        self.name = name
        # 由类内部确定的数据,类外不能修改
        self.__age = 20  # [注意:私有变量]

    @property
    def age(self):
        return self.__age


shuang_er = Wife("双儿")
print(shuang_er.name)
print(shuang_er.age)

# *写法3:只写属性
#      实例变量在类的外部只能修改不能读取
# 快捷键:无
"""
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age 
    # @property # age = property( age   )
    # def age(self):
    #     return self.__age 
    age = property()

    @age.setter
    def age(self, value):
        self.__age = value
 
shuang_er = Wife("双儿", 28)
print(shuang_er.__dict__)
print(shuang_er.name)
# print(shuang_er.age)
"""
