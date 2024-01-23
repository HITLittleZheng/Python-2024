"""
    列表：由一系列变量组成的可变序列容器。
    字典：由一系列键值对组成的可变散列容器。
"""
# 1. 创建
# 列表存储单一维度数据
list_name = ["万雪梅", "孙永鑫", "张琪"]
list_age = [28, 25, 26]
list_sex = ["女", "男", "女"]
# 字典存储多个维度数据
# -- 根据键值对
dict_wxm = {"name": "万雪梅", "age": 28, "sex": "女"}
dict_syx = {"name": "孙永鑫", "age": 25, "sex": "男"}
dict_zq = {"name": "张琪", "age": 26, "sex": "女"}
# -- 根据可迭代对象
# 注意：对可迭代对象元素的格式要求：能够一分二
list_name = [("万", "雪梅"), ["孙", "永鑫"], "张琪"]
print(dict(list_name))
# 2. 添加   字典[键] = 值
if "money" not in dict_wxm:
    dict_wxm["money"] = 10000000
# 3. 定位：字典[键]
# -- 修改
if "age" in dict_wxm:
    dict_wxm["age"] = 26
# -- 读取
if "name" in dict_wxm:
    print(dict_wxm["name"])
print(dict_wxm)
