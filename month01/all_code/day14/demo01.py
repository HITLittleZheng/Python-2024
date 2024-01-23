"""

"""

# 老张开车去东北
# 　增加新功能：开飞机／划船／骑自行车．．．
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print(self.name, "去", position)
        if type(vehicle) == Car:
            vehicle.run()
        elif  type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("汽车嘟嘟嘟...在行驶")

class Airplane:
    def fly(self):
        print("飞机嗖嗖嗖...在飞行")

zl = Person("老张")
car = Car()
air = Airplane()
zl.go_to("东北", car)
zl.go_to("东北", air)
"""

# def func01():
#     pass
#
# func01() # 调用/执行 func01

# -------------架构师------------------
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        # 传入的对象 是一种 交通工具
        if isinstance(vehicle, Vehicle):
            # "我要调用变化点"
            # 编码时:调用的是父(Vehicle)
            # 运行时:执行的是子(Car或者Airplane)
            vehicle.transport()


class Vehicle:
    def transport(self):
        pass


# -------------程序员------------------

class Car(Vehicle):
    # 重写:子类具有和父类相同的方法
    def transport(self):
        print("汽车嘟嘟嘟...在行驶")


class Airplane(Vehicle):
    # 重写的快捷键:ctrl + o
    def transport(self):
        print("飞机嗖嗖嗖...在飞行")


# -------------测试------------------
lz = Person("老张")
car = Car()
lz.go_to("东北", car)
lz.go_to("东北", Airplane())
lz.go_to("东北", "轮船")










