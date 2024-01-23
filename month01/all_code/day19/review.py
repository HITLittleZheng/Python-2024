"""
    实例成员
        对象.成员名
"""


# 抽象化
class Wife:
    def __init__(self, name=""):
        # 为对象创建实例变量(对象的数据)
        self.name = name

    # 实例方法:操作实例变量(参数必须有self)
    def work(self):
        # 在类中通过self访问实例成员
        print(self.name,"在工作")

# 具体化
# 对象名 = 类名(数据)
shuanger = Wife("双儿") # 自动调用构造函数
# 在类外通过对象名访问实例成员
print(shuanger.name)
shuanger.work()

ake = Wife("阿珂")
print(ake.name)
ake.work()

