"""
    字典：
        增加/修改键值对
"""
dict01 = {"name": "Python", "age": 18}

# 1. 增加|修改
#   　字典名[键] = 值
#     键不存在为增加, 键存在为修改该键对应的值
# 键不存在
dict01['score'] = 100
print(dict01)

# 键存在
dict01['score'] = 99
print(dict01)

# 2. 修改
#     字典名.setdefault(key, default=None)
#       key：　要修改的键
#       default：默认值, 默认为None, 键不存在则取默认值
#     返回值: 健存在获取键对应的值, 键不存在则取默认值

# 键存在
res = dict01.setdefault("age")
print(res, dict01)

# 键不存在
res = dict01.setdefault("info", "no info")
print(res)
print(dict01)
