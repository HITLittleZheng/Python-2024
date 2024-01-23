"""
    列表
        增加元素
            指定位置插入元素：
            尾部追加：
        删除元素
"""
list_01 = ['Python', 'Java', 'C', 'C++', 'MySQL', 'PHP']

# 增加元素
#   -- 指定位置插入元素  列表名.insert(index, value)
list_01.insert(0, 'AID')

print(list_01)  # ['AID', 'Python', 'Java', 'C', 'C++', 'MySQL', 'PHP']
list_01.insert(1, 'tedu')
print(list_01)

#  -- 末尾追加  列表名.append(value)
list_01.append("Numpy")
print(list_01)

# 删除元素
#   -- 删除指定索引的元素
#       列表名.pop(index=-1) 默认为-1 删除最后一个元素
#       返回值为：删除的元素
list_01.pop()
print(list_01)

list_01.pop(1)
print(list_01)

# list_01.pop(100) # IndexError: pop index out of range
# print(list_01)

#   -- 删除指定元素
#       列表名.remove(元素)
#       删除元素不存在，则出发ValueError异常
list_01.remove('PHP')
print(list_01)
# list_01.remove('ABC')
