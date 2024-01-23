"""
    函数
"""
# 重复的代码就是万恶之源(遇到变化时,需要修改多段代码)
"""
# 做法(变化) + 用法
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
print("鞭腿")
# ...
# 做法(变化) + 用法
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
print("鞭腿")
"""


# 做法(变化)
def attack():
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")
    print("鞭腿")
    print("逃跑")

# 用法
attack()
# ...
attack()
