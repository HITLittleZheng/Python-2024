"""

"""


class Commodity(object):
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}的编号是{self.cid},单价是{self.price}"


class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return "%s的攻击力是%s,血量是%s" % (self.name, self.atk, self.hp)


cmd = Commodity(1001, "屠龙刀", 10000)
enemy = Enemy("灭霸", 100, 500)
# 直接打印自定义对象
# <__main__.Commodity object at 0x7faf1a1b65f8>
# 编码时:调用
# 运行时:执行商品的__str__方法
print(cmd)
# <__main__.Enemy object at 0x7faf1a1b6630>
print(enemy)
