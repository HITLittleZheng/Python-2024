"""
    列表 list：
        由一系列变量组成的可变序列容器
"""

# 1. 创建列表
#   -- 空列表
list_01 = []
list_02 = list()
print(list_01, type(list_01))
print(list_02, type(list_02))

#   -- 非空列表
name = "唐三藏"
list_03 = [name, "空空", "八戒", "净净", 18, 19.5, True, 3j]
print(list_03, type(list_03))

# 参数必须为可迭代对象
list_04 = list("人工智能")
print(list_04, type(list_04))

list_05 = list(range(10))
print(list_05)

# 2. 定位元素
list_06 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#   -- 定位单个元素 --> 索引  --> 容器名[索引值]
print('索引为0的元素:', list_06[0])
print('索引为1的元素:', list_06[1])
print('索引为-1的元素:', list_06[-1])
print('索引为-5的元素:', list_06[-5])
# IndexError: list index out of range
# print('索引为-5的元素:', list_06[11]) # 索引超出范围

#   -- 定位多个元素 --> 切片  --> 容器名[起始索引:终止索引:步长]
print(list_06[:])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(list_06[1:])  # ['B', 'C', 'D', 'E', 'F', 'G']
print(list_06[1:5])  # ['B', 'C', 'D', 'E']
print(list_06[1:5:2])  # ['B', 'D']
print(list_06[-1:-5:-2])  # ['G', 'E']

# 获取容器长度
print(len(list_06))  # 7


