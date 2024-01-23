"""
    函数
"""


# ------------定义函数-----------------

def attack_repeat(count):  # 2
    list_data = []
    for i in range(count):
        data = attack_single()
        list_data.append(data)
    return list_data


def attack_single():  # 3
    print("直拳")
    print("摆拳")
    print("勾拳")
    return "ok"


# ------------调用函数-----------------
result = attack_repeat(2)  # 1
print(result)  # ??
