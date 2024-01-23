"""
    小明使用手机打电话
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication):
        print(self.name, "打电话")
        # 调用交通工具
        # 执行手机座机
        communication.dialing()


class Communication:
    def dialing(self):
        pass


class MobilePhone(Communication):
    def dialing(self):
        print("手机呼叫")


class Landline():
    def dialing(self):
        print("座机呼叫")


xm = Person("小明")
xm.call(MobilePhone())
xm.call(Landline())
