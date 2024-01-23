"""
    类成员
        类变量:不同对象相同(共享)数据
        类方法:操作类变量
        语法:
            通过类名访问
"""


class ICBC:
    """
        工商银行
    """
    # 类变量:总行的钱
    total_money = 1000000

    @classmethod
    def print_total_money(cls):
        # 建议在类方法中通过参数cls操作类变量
        # print("总行的钱:", ICBC.total_money)
        print("总行的钱:", cls.total_money)

    def __init__(self, name="", money=0):
        # 实例变量:不同支行不同数据
        self.name = name
        self.money = money
        # 支行创建时,总行的钱减少
        ICBC.total_money -= self.money


tian_tan = ICBC("天坛支行", 100000)
# print("总行的钱:", ICBC.total_money)
ICBC.print_total_money()

tao_ran_ting = ICBC("陶然亭支行", 200000)
# print("总行的钱:", ICBC.total_money)
ICBC.print_total_money()
