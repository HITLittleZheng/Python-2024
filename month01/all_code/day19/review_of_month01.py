"""
    一.Python核心
    1. 程序执行过程
        源代码 -- 编译 --> 字节码 -- 解释 --> 机器码
        注意1:第一次运行程序生成字节码(pyc)
            以后运行直接从字节码到机器码(速度更快)
        注意2:主模块(第一次执行的模块)不会生成字节码
             只有被导入模块才会生成字节码
    2. Python语言内存管理机制
        -- 引用计数：每个对象记录被变量绑定的数量，
                   当为0时被销毁。
            缺点:存在循环引用的情况
        -- 标记清除:对内存空间全盘扫描,检查不再使用的数据.
            缺点:速度太慢
        -- 分代回收:将内存分为012(小中大)三代,
                   创建新数据永远在0代分配空间,
                   待内存告急时,触发标记清除,
                   将有用的数据升代,没用的数据释放
        -- 优化内存:
            尽少产生垃圾,对象池,配置垃圾回收器
    3.  身份运算符
    4. 容器
        列表:
            适用性:存储多个单一维度数据
            特点:存储变量,
                可变(增删改/预留空间+按需分配),
                序列(有顺序,支持索引切片),
            语法:
                list01 = []
                list01.append(数据)
                list01.insert(索引,数据)

                del list01[0],list01[:2]
                list01.remove(数据)

                list01[:] = ?  # 修改
                ? = list01[:] # 读取:切片读取时触发浅拷贝

                for item in list01:#从头到尾读
                for i in range(len(list01)):
        字典:
            适用性:存储多个多个维度数据
            特点:存储键值对,
                可变(增删改/预留空间+按需分配),
                散列(无顺序,定位单个元素速度最快),
            语法:
                dict01 = {}
                dict01[键] = 值

                del dict01[键]

                dict01[键] # 定位

                for k in dict01:
                for v in dict01.values():
                for k,v in dict01.items():
        字典转换为列表:
            list(dict01)
            list(dict01.values())
            list(dict01.items())
        列表转换为字典:
            dict(  [(键,值)]    )
    5. 类型标注
        价值:
            为变量增加类型
        语法:
         变量名:数据类型
         def 函数名(参数)->数据类型:
         # type:int

        作用:
         增加操作提示
         类型检测

    6. 软件编程三大范式:
        面向过程:考虑问题从步骤出发
                例如:排序(取数据/作比较/找更大/则交换))
        面向对象:考虑问题从对象出发(谁?干嘛?)
                例如:MVC
        函数式编程:
                将函数作为参数
                例如:排序(  根据薪资排序,    根据部门排序)
                      lambda e:e.money  lambda e:e.did
        核心目标:满足开闭原则
                (分/隔/做)
"""
# 循环引用:2个列表相互存储对方,
#         但是操作列表的变量却被删除了
#        所以2个列表(垃圾)长期占用内存,不能释放
from typing import List

list01 = []
list02 = []
list01.append(list02)
list02.append(list01)

# 程序员的意思:2个列表都不再使用
# 但列表的引用计数为1,不会被销毁.
del list01, list02

# 内置对象池:int/float/bool/str
# 每次创建数据时,都先在池中判断,是否具有相同数据
# 如果有直接返回地址,没有再开辟空间.
# 优点:相同数据在内存中存储一份,从而节省内存
data01 = "悟空"
data02 = "悟空"
print(id(data01))
print(id(data02))

"""
class 自定义对象池:
    def __init__(self):
        self.对象池 = []

    def 创建数据(self):
        先判断列表中是否存在可用数据
        如果可用直接返回数据地址
        从列表中删除该数据
"""

# 3.身份运算符
list01 = [10]
list02 = [10]
# 判断数据内容
# list01.__eq__(list02)
print(list01 == list02)  # True
# 判断变量地址
print(list01 is list02)  # False


class Wife:
    def __init__(self, name=""):
        self.name = name

    def __eq__(self, other):
        # 默认比较地址
        # return id(self) == id(other)
        # 按照内容比较
        return self.name == other.name


shuang_er1 = Wife("双儿")
shuang_er2 = Wife("双儿")
print(shuang_er1 == shuang_er2)  # False

list01 = ["a", "b", "c"]
# 依次将右侧可迭代对象元素取出  (正向)
# 存储到左侧定位区域       (反向)
list01[::-1] = [1, 2, 3]
print(list01)


# 没类型就意味着没操作提示
# 语法:
#  变量名:数据类型
#  def 函数名(参数)->数据类型:
#  # type:int

# 作用:
#  增加操作提示
#  类型检测

def func01(p1: str) -> int:
    pass


class Controller:
    def __init__(self, data1):
        self.data1 = data1  # type:int
        self.data2 = []  # type:List[str]


c = Controller(10)
for item in c.data2:
    pass

import time

print(time.mktime((1949, 11, 24, 0, 0, 0, 0, 0, 0)))

"""
    面向对象:老张开车去东北 
class Person: 
    def go_to(self, vehicle):
        vehicle.transport() 
class Vehicle:
    def transport(self):
        pass  
class Car(Vehicle): 
    def transport(self):
        print("汽车嘟嘟嘟...在行驶")   
class Airplane(Vehicle): 
    def transport(self):
        print("飞机嗖嗖嗖...在飞行") 
lz = Person()
lz.go_to(Car())
"""


# 函数式编程:老张开车去东北
# (仅限于实现过程简单到一句话)
class Person:
    def go_to(self, transport):
        transport()


lz = Person()
lz.go_to(lambda: print("汽车嘟嘟嘟...在行驶"))
lz.go_to(lambda: print("飞机嗖嗖嗖...在飞行"))
