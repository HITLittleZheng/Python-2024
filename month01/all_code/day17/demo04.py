"""
    生成器表达式
        列表推导式"升级版"(节省内存)

    列表
        优点:操作数据方便
        缺点:占用内存较多
    生成器
        优点:占用内存较少
        缺点:操作数据不方便
            (不能使用索引/切片,不能删除修改,只能使用一次)
        适用性:从头到尾读取一次
              (优先)
        解决:转换为列表
            list(生成器)
            tuple(生成器)
            set(生成器)
"""
# 将列表中大于10的数字存入另外一个列表
list01 = [4, 54, 65, 67, 78, 8, 9]
generator01 = (item for item in list01 if item > 10)
for item in generator01:
    print(item)

# 将列表中所有数字的个位存入另外一个列表
generator02 = (item % 10 for item in list01)
for item in generator02:
    print(item)
