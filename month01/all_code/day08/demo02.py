"""
    函数 - 参数
"""

# 做法
def attack(count):  # 形参：抽象、不真实
    for i in range(count):
        print("直拳")
        print("摆拳")
        print("勾拳")

# 用法
attack(2)  # 实参：具体、真实
print("后续逻辑")
attack(1)
