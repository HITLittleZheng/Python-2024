"""　
    列表list
"""
# 5. 删除
list_names = ["石奇", "涂洋涛", "张琪"]
# -- 根据元素删除
if "琪琪" in list_names:
    list_names.remove("琪琪")  # 如果不存在则报错
# -- 根据定位删除
del list_names[0], list_names[:]
print(list_names)
