"""
    在之前的基础上,增加数据.
        手雷具有攻击力,玩家和敌人有血量
"""


# ----------架构师------------
class Grenade:
    def __init__(self, atk=0):
        self.atk = atk

    def explode(self, target):
        print("爆炸")
        target.damage(self.atk)


class AttackTarget:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self,value):
        self.hp -= value


# ----------程序员------------
class Player(AttackTarget):
    def damage(self,value):
        print("碎屏")
        super().damage(value)


class Enemy(AttackTarget):
    def damage(self,value):
        print("头顶爆字")
        super().damage(value)


# ----------测试------------
grenade = Grenade(100)
p = Player(200)
grenade.explode(p)
e = Enemy(100)
grenade.explode(e)
print(p.hp)
print(e.hp)

