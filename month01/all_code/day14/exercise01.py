"""
    练习1：以面向对象思想，描述下列情景：
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
"""


# ----------架构师------------
class Grenade:
    def explode(self, target):
        print("爆炸")
        # 编码时:调用父
        # 运行时:执行子
        target.damage()


class AttackTarget:
    def damage(self):
        pass


# ----------程序员------------
class Player(AttackTarget):
    def damage(self):
        print("碎屏")


class Enemy:
    def damage(self):
        print("头顶爆字")


# ----------测试------------
grenade = Grenade()
grenade.explode(Player())
grenade.explode(Enemy())
