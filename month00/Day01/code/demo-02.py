"""
    需求： 通过python 实现汇率转换器
    步骤：
        1. 明确需求：
            a. 接受用户输入的美元数
            b. 使用 用户输入的美元数 * 6.3944
            c. 打印输出计算结果
        2. 编码、调试：
    结论：
        1. 程序不是写出来的，改出来的
        2. 码代码的过程：先分析再码
        3. 从右至左，从上之下
    编码规范：
        ctrl + alt + l
"""
# a.接受用户输入的美元数
usd_str = input('请输入美元数：')

# b.使用用户输入的美元数 * 6.3944
usd_int = int(usd_str)
rmb = usd_int * 6.3944

# c.打印输出计算结果
print(rmb)
