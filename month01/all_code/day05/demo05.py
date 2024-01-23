"""
    拷贝：复制,备份,一份变两份的过程,防止数据被意外修改.
    浅拷贝：第一层数据拷贝,深层数据共享
        优点：占用内存较少
        缺点：深层数据被修改,互相影响.
        适用性：优先
    深拷贝：所有层数据拷贝
        优点：绝对互不影响
        缺点：占用内存较多
        适用性：当深层数据需要被修改时
"""

# 准备深拷贝工具
import copy

list01 = [10, [20, 30, 40]]
list02 = copy.deepcopy(list01)
list02[0] = 100  # 修改第一层，
list02[1][0] = 200  # 修改深层,
print(list01)