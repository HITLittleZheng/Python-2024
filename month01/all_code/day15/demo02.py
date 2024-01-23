"""
    小结 - 面向对象
        语法
            1. 类和对象
                class 类名:
                    类变量 = 数据

                    @classmethod
                    def 类方法(self,参数):
                        操作类变量

                    def __init__(self,参数):
                        self.实例变量 = 参数

                    def 实例方法(self,参数):
                        操作实例变量

                对象名 = 类名(数据)
                对象名.实例成员
                类名.类成员
            2. 封装
                私有化:命名以下划线开头,类外无法访问
                属性:保护实例变量
                    读写属性快捷键:props
                    @property
                    def 属性名(self):
                        return self.私有变量

                    @属性名.setter
                    def 属性名(self, value):
                        self.私有变量 = value

                    只读性快捷键:prop
                    @property
                    def 属性名(self):
                        return self.私有变量
            3. 继承
                class 儿子(爸爸):
                    def __init__(self,爸爸的参数,自己的参数):
                        super().__init__(爸爸的参数)
                        self.实例变量=自己的参数

                    def 自己的实例方法(self):
                        self.爸爸的方法()

                    # 重写:子类拥有和父类相同的方法
                    def 重写方法(self):
                        super().重写方法()

                # 执行子类构造函数,再执行父类构造函数
                对象名 = 儿子(数据)
            4. 多态
                def 客户端代码(爸爸):
                    (1)调用父
                    爸爸.方法()

                class 父类:
                    def 方法(self):
                        pass

                class 大儿子(父类):
                    (2)子重写
                     def 方法(self):
                        具体功能

                (3)创建子
                客户端代码(大儿子())

        思想
            字面意思:考虑问题从对象的角度出发
                    "找人 干活"
            需求:老张开车去东北
            封装[分]:
                根据需求划分多个类
                分而治之,变则疏之
                例如-创建人类/车类/飞机类...
            继承[隔]:
                隔离客户端代码与变化点
            多态[做]:
                以重写的方式实现具体功能
"""


# 读写属性
class MyClass:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


m = MyClass(10)
m.data = 20
print(m.data)

# 只读属性:为私有变量提供读取功能
class MyClass:
    def __init__(self):
        self.__data = 10

    @property
    def data(self):
        return self.__data

m = MyClass()
print(m.data)
