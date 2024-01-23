"""
    跨类调用
        两个类互相调用(协作)
"""


"""
# 面向过程
def go_to(position): # 2
    print("去", position)
    run()

def run(): # 3
    print("汽车嘟嘟嘟...在行驶")

go_to("东北") # 1
"""

# 以面向对象的思想,描述情景: 老张开车去东北
# 写法1:直接创建对象
# 语义:老张每次开一辆新车去东北
"""
# -------------定义类----------------

class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position):
        print(self.name, "去", position)
        car = Car()
        car.run()

class Car:
    def run(self):
        print("汽车嘟嘟嘟...在行驶")

# -------------入口----------------
zl = Person("老张")
zl.go_to("东北")
zl.go_to("北京")
"""

# 写法2: 在构造函数中创建对象
# 语义:老张开自己的车去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        # 一个人只执行一次构造函数
        self.car = Car()

    def go_to(self, position):
        print(self.name, "去", position) 
        self.car.run()

class Car:
    def run(self):
        print("汽车嘟嘟嘟...在行驶")

# -------------入口----------------
zl = Person("老张")
zl.go_to("东北")
zl.go_to("北京")
"""

# 写法3: 通过参数传递对象
# 语义:老张通过交通工具去东北
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position,vehicle):
        print(self.name, "去", position)
        vehicle.run()

class Car:
    def run(self):
        print("汽车嘟嘟嘟...在行驶")

zl = Person("老张")
car = Car()
zl.go_to("东北",car)