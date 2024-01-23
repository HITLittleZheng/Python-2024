"""
    内置生成器
"""
list01 = [54, 0, 65, 65, 7, 0]
# 快捷键:iter + 回车
# 从头到尾读取
for item in list01:
    print(item)

# 从头到尾修改
for i in range(len(list01)):
    if list01[i] == 0:
        list01[i] = 10

# 快捷键:itere + 回车
# 每次返回的是一个元组(第一个元素是索引,第二个元素是元素)
# for item in enumerate(list01):
#     print(item)
for i, item in enumerate(list01):
    if item == 0:
        list01[i] = 10

