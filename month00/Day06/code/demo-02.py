"""
    list --> str
        str.join(iterable)
            将字符串类型的可迭代对象依据一定的字符进行连接
            iterable： 元素为字符串类型的可迭代对象
            返回值：拼接后的字符串
"""
address = ['北京', '东城区', '珍贝大厦']

# 按照-连接列表中的元素
new_add = '-'.join(address)
print('new_address ', new_add)

# 按照空连接列表中的元素
new_add = ''.join(address)
print('new_address ', new_add)

# 注意：不能连接整型的
# L = range(1,3)
# print('/'.join(L))
