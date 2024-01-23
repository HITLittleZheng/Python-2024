"""
    闭包-应用
        逻辑连续
            从得2000元钱,到不断购买商品的过程连续不中断.
"""

def get_new_year_money(money):
    print(f"获得了{money}元压岁钱")

    def child_buy(commodity, price):
        nonlocal money
        money -= price
        print(f"孩子花了{price}元购买了{commodity},还剩下{money}")

    return child_buy


action = get_new_year_money(2000)
action("游戏机", 500)
action("电脑", 1000)
action("手机", 300)
