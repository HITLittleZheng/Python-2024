"""
    列表操作：

"""
list_01 = ['Python', 'Java', 'C', 'C++', 'MySQL', 'PHP']

# 修改操作
#   -- 单个元素修改 --> 列表名[索引]= 值
list_01[-1] = 'JavaScript'
print(list_01)

#   -- 多个元素修改 --> 列表名[起始:结束:步长] = 可迭代对象
list_01[::2] = [1, 2, 3]
print(list_01)

# 切片元素个数 < 值的个数, 产生 ValueError
# ValueError: attempt to assign sequence of size 2 to extended slice of size 3
list_01[::2] = "abc"
print(list_01)
