"""
    列表推导式嵌套
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["雪碧", "牛奶", "咖啡", "果汁"]
# list_new = []
# for r in list01:  # 香蕉                   苹果
#     for c in list02:  # 雪碧 牛奶 咖啡 果汁     雪碧 牛奶 咖啡 果汁
#         list_new.append((r, c))
# print(list_new)
list_new = [(r, c) for r in list01 for c in list02]
print(list_new)




