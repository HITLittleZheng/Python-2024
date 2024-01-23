"""
    continue 语句:
        跳过本次循环，直接继续下一次循环
    说明：
        1. continue语句执行后,将不再执行本次循环内continue之后的语句
        2. continue语句 适用于循环语句(for/while)
            while 循环中, 执行continue 将会直接从continue跳转到条件表达处

    需求：
        输入两个数, 分别代表起始值 和 终止值.
        根据 输入值大小,可以升序 或 降价打印输入。
        遇到 4 跳过 不输出
"""

start = int(input("请输入起始值:"))
end = int(input("请输入终止值:"))

while start <= end:
    start += 1
    if start == 4:
        continue  # 跳过本次循环

    print(start, end=" ")

