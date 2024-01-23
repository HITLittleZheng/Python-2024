"""
    列表list：由一系列变量组成的可变序列容器。
    元组tuple：由一系列变量组成的不可变序列容器。
"""
# 创建
# -- 根据元素
tuple_week = ("星期一", "星期二", "星期三")
# -- 根据可迭代对象
list_name = ["张琪", "徐浩"]  # 存储计算过程中的数据
tuple_name = tuple(list_name)  # 存储计算结果

# 定位(只读)
# --索引
print(tuple_week[-1])
# tuple_week[0] ="星期1" # 元组不支持赋值
# --切片(读取数据触发浅拷贝)
print(tuple_week[:2])
print(tuple_week[-2:])

# 遍历
for item in tuple_week:
    print(item)

for i in range(len(tuple_week) - 1, -1, -1):
    print(tuple_week[i])

# 注意1:创建元组的括号在没有歧义的情况下可以省略
tuple_week = "星期一", "星期二", "星期三"
print(tuple_week)
# 注意2:如果元组中只有一个元素,必须添加逗号
tuple_number = (10,)
print(type(tuple_number))
# 注意3:序列拆包
a, b, c = tuple_week
a, b, c = ["A", "B", "C"]
a, b, c = "孙悟空"
print(a)
print(b)
print(c)

# 注意:元组增加元素会创建新元组
tuple01 = (10, 20)
tuple01 += (30,)
print(tuple01) # (10, 20, 30, 40)
