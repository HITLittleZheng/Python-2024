"""
    练习2：以面向对象思想,描述下列情景.
    玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).
"""
"""
class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self,target):
        print("发起攻击")
        # 玩家打敌人时,传递了自身
        # (敌人拥有了玩家的所有数据)
        target.damage(self)

class Enemy:
    def __init__(self, hp = 0):
        self.hp = hp

    def damage(self,other):
        print("头顶爆字")
        self.hp -= other.atk
"""


class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self, target):
        print("发起攻击")
        # 玩家打敌人时,传递了敌人必须知道的信息
        target.damage(self.atk)


class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        print("头顶爆字")
        self.hp -= value


p = Player(50)
e = Enemy(100)
p.attack(e)
print(e.hp)
