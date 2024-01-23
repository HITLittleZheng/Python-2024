"""
    需求： 通过python 实现汇率转换器
"""
# 1. 获取数据
usd_str = input("请输入金额：")

# 2. 逻辑计算
usd_float = float(usd_str)
rmb = usd_float * 6.3947

# 3. 显示结果
print(rmb)