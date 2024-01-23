"""
    字典
        一系列 键值对 组成的 可变 散列容器
"""

# 1. 创建字典
#   -- 创建空字典
d = {}
print(d, type(d))

d1 = dict()
print(d1, type(d1))

#   -- 创建非空
#   注意：字典的键 为不可变类型; 键不能重复
#       值不限制类型
d3 = {"name": "百万", "age": 18, True: [1, 3, 5]}
print(d3, type(d3))

#  dict() 可迭代对象创建新字典

#   dict(**kwargs)
d4 = dict(a=100, b=200)
print(d4, type(d4))  # {'a':100, 'b':200}

d5 = dict([["name", "python"]])
print(d5, type(d5))

