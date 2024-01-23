"""
    列表
        创建
            列表名 = [数据1,数据2]
            列表名 = list(可迭代对象)
        添加
            列表名.append(元素)
            列表名.insert(索引,元素)
        定位
            列表[整数]
            列表[整数:整数:整数]
        遍历
            for 变量 in 列表:
            for i in range(...):
        删除
            列表名.remove(元素)
            del 列表[整数],列表[整数:整数:整数]
"""
list01 = [4, 5, 6, 7, 8, 9]
# # 只能从头到尾读取元素,不能修改
# for item in list01:
#     if item % 2:
#         item = 0
# print(list01)

for i in range(len(list01)):# 0 1 2 ... len(list01)-1
    if list01[i] % 2:
        list01[i] = 0
print(list01)


for i in range(len(list01)-1,-1,-1):
    print(list01[i])