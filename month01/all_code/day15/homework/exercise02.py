"""

"""

"""
class Player:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def attack(self, target):
        print("发起攻击")
        target.damage(self.atk)

    def damage(self, value):
        print("碎屏")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("充值")


class Enemy:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def attack(self, target):
        print("发起攻击")
        target.damage(self.atk)

    def damage(self, value):
        print("头顶爆字")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("加分")


# --------------测试--------------
p = Player(200, 50)
e = Enemy(100, 10)
p.attack(e)
e.attack(p)

p.attack(e)
"""

class Character:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def attack(self, target):
        print("发起攻击")
        target.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        pass

class Player(Character):
    def damage(self, value):
        print("碎屏")
        super().damage(value)

    def death(self):
        print("充值")

class Enemy(Character):
    def damage(self, value):
        print("头顶爆字")
        super().damage(value)

    def death(self):
        print("加分")


# --------------测试--------------
p = Player(200, 50)
e = Enemy(100, 10)
p.attack(e)
e.attack(p)

p.attack(e)










