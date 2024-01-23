"""
    练习1：创建敌人类，并保护数据在有效范围内
     数据：姓名、攻击力、血量
​               0-100   0-500
"""


class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def set_atk(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        self.__atk = value

    def get_atk(self):
        return self.__atk

    atk = property(get_atk, set_atk)

    def set_hp(self, value):
        if value < 0:
            value = 0
        elif value > 500:
            value = 500
        self.__hp = value

    def get_hp(self):
        return self.__hp

    hp = property(get_hp, set_hp)


mie_ba = Enemy("灭霸", 800, 1000)
print(mie_ba.atk)
print(mie_ba.hp)
