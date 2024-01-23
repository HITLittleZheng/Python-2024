"""
    结论:
        函数有单个结果:
            传统思想-使用return返回容器
        函数有多个结果:
            生成器思想-使用yield返回元素
"""

list01 = [34, 54, 65, 76, 87, 98, 9, 59]


# 创建函数,在列表中查找大于10的所有数据.
# 传统思想:创建容器存储所有结果
# 缺点:占用内存太多
def find_all_gt_10():
    result = []
    for item in list01:
        if item > 10:
            result.append(item)
    return result

# data = find_all_gt_10()
# for item in data:
#     print(item)


# 生成器思想:几乎不占内存
def find_all_gt_10():
    for item in list01:
        if item > 10:
            yield item


data = find_all_gt_10()
for item in data:
    print(item)
# 生成器只能用一次
for item in data:
    print(item)
# 解决方案:
data = list(find_all_gt_10())
for item in data:
    print(item)
for item in data:
    print(item)