"""　
    列表list
"""
# 3. 定位(读取/修改)
list_names = ["石奇", "涂洋涛", "张琪"]
# -- 索引
print(list_names[0])
list_names[1] = "洋涛"
# -- 切片
# 通过切片读取数据,会创建新列表存储结果
print(list_names[-2:])
# 通过切片修改数据,将右侧可迭代对象数据依次存入左侧
list_names[-2:] = ["洋洋", "琪琪"]
# list_names[-2:] = 10
# list_names[-2:] = "悟空"
# list_names[1:1] = "齐天大圣孙悟空"
# list_names[:] = ""
print(list_names)

# 4. 遍历
# -- 从头到尾获取所有元素
for item in list_names:
    # 打印列表中第一个字和最后一个字相同的人名
    if item[0] == item[-1]:
        print(item)

# -- 非从头到尾获取所有元素
# 倒序查找数据
# for item in list_names[::-1]:
#     print(item)

# len(list_names) - 1:从总数减一开始
# -1:不包含负一,包含零
# -1:倒序
for i in range(len(list_names) - 1, -1, -1):
    print(list_names[i])
