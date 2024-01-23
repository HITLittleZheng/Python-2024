"""
    字典
        查看:
            通过键 获取值
                字典名[键]  --> 如果键不存在, 出发 KeyError
                字典名.get(键, 默认值)
                    如果键不存在, 返回默认值, 默认为None
"""
dict01 = {"name": "Python", "age": 18, "address": "Beijing"}
print(dict01)

# 1. 通过键 获取值
#       字典名[键]
#       键不存在则触发异常： KeyError
print(dict01['name'])
print(dict01['address'])

# 2. 获取值
#       字典名.get(key, default=None)
#       通过key 获取对应的value, 如果key 不存在 则默认返回None
#       key 不存在 可以指定默认值
print(dict01.get('age'))
print(dict01.get('age1'))  # key 不存在 返回None
print(dict01.get('age1', 'no age1'))  # key 不存在　指定默认值

# 3. 判断 键是否存在
#    in   /  not in
#    返回值：布尔类型
dict01 = {"name": "Python", "age": 18, "address": "Beijing"}
print("name" in dict01)
print("NAME" not in dict01)
