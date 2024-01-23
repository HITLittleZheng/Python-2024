"""　
    列表list：由一系列变量组成的可变序列容器。
        用于存储单一维度的数据
        例如:姓名列表
"""
# 1. 创建
# -- 根据元素
list_names = ["石奇", "涂洋涛", "张琪"]
list_ages = [28, 26, 27]
list_sexs = ["男", "女", "女"]
# -- 根据可迭代对象(将不可变数据改为可变数据)
list_swk = list("孙悟空")
print(list_swk)

# 2. 添加
# -- 追加
list_names.append("张超")
list_ages.append(30)
list_sexs.append("女")
# -- 插入
list_names.insert(0,"李阳")
list_ages.insert(0,24)
list_sexs.insert(0,"男")
