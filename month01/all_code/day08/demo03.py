"""
    函数-返回值
"""
# 设计理念：崇尚小而精,拒绝大而全

# 需求：创建2个数值相加的函数
"""
# 大而全的函数
def add():
    # 获取数据
    number01 = int(input("请输入第一个数字："))
    number02 = int(input("请输入第二个数字："))
    # 逻辑计算
    result = number01 + number02
    # 显示结果
    print("结果是：" + str(result))

add()
"""


def add(number01, number02):
    # 逻辑计算
    result = number01 + number02
    # 显示结果
    # print("结果是：" + str(result))
    # 返回结果
    return result

number = add(5,3)
print(number)
