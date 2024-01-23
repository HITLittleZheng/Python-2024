"""
    str  --> list
    str.split(sep=None, maxsplit=-1)
        将字符串依据一定的规格按照指定个数进行分割.
        sep: 分割的依据
        maxsplit：分割的最大条目,默认全部分割
    返回值：分割后的列表
"""
website = "http://www.baidu.com"

# 按 . 全部分割
res = website.split('.')
print(res)

res = website.split('.', 1)
print(res)

# 按照空格全部分割
string = 'h el lo wo rl d'
res = string.split(" ")
print(res)
# 默认按照空格进行分割, 丢弃空字符串
res = string.split()
print(res)