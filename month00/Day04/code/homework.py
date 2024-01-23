"""
    模拟出租车计价器
        1. 起步价: 13元包含3公里.
        2. 超过3公里, 但是没有超过15公里: 每公里2.3元.
        3. 如果超过15公里: 每公里加收2.3元的50%.
        要求：计算的最终费用 保留两位小数.

    完成之后, 复习今天知识, 操作 debug 调试模式[多操作几遍]。
"""
# 1. 获取数据
# km = float(input("请输入一个公里数："))
# price = 13

# 2. 逻辑计算
# if 0 < km <= 3:
#     price = price
#
# elif 3 < km <= 15:
#     # price = (km - 3) * 2.3 + price
#     price += (km - 3) * 2.3
#
# elif km > 15:
#     # price = price + 12 * 2.3 + (km - 15) * 2.3 * 1.5
#     price += 12 * 2.3 + (km - 15) * 2.3 * 1.5
#
#
# # 3. 打印输出
# print("费用", round(price, 2))

# 代码优化：
km = float(input("请输入一个公里数："))
price = 13

if km > 0:
    if 0 < km <= 3:
        price = price

    elif 3 < km <= 15:
        # price = (km - 3) * 2.3 + price
        price += (km - 3) * 2.3

    elif km > 15:
        # price = price + 12 * 2.3 + (km - 15) * 2.3 * 1.5
        price += 12 * 2.3 + (km - 15) * 2.3 * 1.5

    print("费用", round(price, 2))

else:
    print("公里数有误！")

