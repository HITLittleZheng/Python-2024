"""

"""
import copy

list01 = ["北京", ["上海", "深圳"]]
list02 = list01  # 赋值,数据1份,互相影响
list03 = list01[:]  # 浅拷贝,第一层数据2份,互不影响;深层数据1份,互相影响
list04 = copy.deepcopy(list01)  # 深拷贝,数据2份,互不影响
list04[0] = "北京04"
list04[1][1] = "深圳04"
print(list01)  # ?

list03[0] = "北京03"  # 修改第一层
list03[1][1] = "深圳03"  # 修改深层
print(list01)  # ?

list02[0] = "北京02"
list02[1][1] = "深圳02"
print(list01)  # ?
