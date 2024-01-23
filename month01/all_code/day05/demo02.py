"""
    列表内存图
"""
list01 = [10, 20, 30]
data01 = list01
data02 = list01[0]
data03 = list01[:2] # 创建新容器

data03[1] = 200 # 数据两份,互不影响
data02 = 100 # 修改变量data02,与列表无关
data01[2] = 300
print(list01) #  数据一份,互相影响


