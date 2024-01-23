"""
    字典
"""
# 4. 删除
dict_wxm = {"name": "万雪梅", "age": 28, "sex": "女"}
del dict_wxm["sex"]
# 5. 遍历
dict_syx = {"name": "孙永鑫", "age": 25, "sex": "男"}
# -- 获取所有key
for key in dict_syx:
    print(key)
# -- 获取所有value
for value in dict_syx.values():
    print(value)
# -- 获取所有key和value
# 元组(键,值)
# for item in dict_syx.items():
#     print(item)
for k, v in dict_syx.items():
    print(k)
    print(v)

# 字典 --> 列表
print(list(dict_syx))  # ['name', 'age', 'sex']
print(list(dict_syx.values()))  # ['孙永鑫', 25, '男']
print(list(dict_syx.items()))  # [('name', '孙永鑫'), ('age', 25), ('sex', '男')]
