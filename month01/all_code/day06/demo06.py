"""
    字典：
        由一系列键值对组成的可变散列容器。
    集合set：
        由一系列　键　组成的可变散列容器。
        应用1:去重复
            去重后的集合 = set(可迭代对象)
"""
# 创建
list_name = ["张琪", "孙永鑫", "张琪", "万雪梅", "张琪"]
dict_syx = {"name": "孙永鑫", "money": 10000000}
# -- 根据元素
set_name = {"张琪", "孙永鑫", "张琪", "万雪梅", "张琪"}
# -- 根据可迭代对象(字符串、列表、元组、字典、集合、range)
print(set(list_name))

# 添加
set_name.add("吉宇轩")

# 删除
# set_name.remove("鑫鑫") # 不存在会报错
set_name.discard("鑫鑫")  # 不存在也没事

# 遍历
for item in set_name:
    print(item)
# 注意：
# 创建空集合
# set01 = {  } # 是字典
set01 = set()
print(type(set01))
