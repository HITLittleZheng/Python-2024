"""
    练习2：定义函数,根据总两数,计算几斤零几两.:
    total_liang = int(input("请输入两:"))
    jin = total_liang // 16
    liang = total_liang % 16
    print(str(jin) + "斤零" + str(liang) + "两")
"""


def calculate_weight(total_liang):
    """
        计算重量
    :param total_liang: int类型,总两数
    :return: 元组类型,(斤,两)
    """
    jin = total_liang // 16
    liang = total_liang % 16
    # return (jin, liang)
    return jin, liang

# weight = calculate_weight(100)
j,l = calculate_weight(100)
print(j)
print(l)