"""
    小结 - 算法
        1. 循环计数
            开始
            for/while...
                间隔
            结束
        2. 交换
            a,b = b,a
        3. 最值
        list01 = [5, 65, 76, 87, 89, 9]
        max_value = list01[0]
        for i in range(1, len(list01)):
            if max_value < list01[i]:
                max_value = list01[i]
        print(max_value)
        4. 自定义排序算法
"""
list01 = [5, 65, 76, 87, 4, 9]
"""
# 第一个元素是最大值
for i in range(1, len(list01)):
    if list01[0] < list01[i]:
        list01[0], list01[i] = list01[i], list01[0]
print(list01)
# [89, 5, 65, 76, 87, 9] 
# 第二个元素是最大值
for i in range(2, len(list01)):
    if list01[1] < list01[i]:
        list01[1], list01[i] = list01[i], list01[1]
print(list01)
# [89, 87, 5, 65, 76, 9]
# 第三个元素是最大值
for i in range(3, len(list01)):
    if list01[2] < list01[i]:
        list01[2], list01[i] = list01[i], list01[2]
print(list01)
# [89, 87, 76, 5, 65, 9]
"""

# 取数据
for r in range(len(list01) - 1):  #       0     1    2
    # 作比较
    for c in range(r + 1, len(list01)):# 123   23   3
        # 找更大
        if list01[r] < list01[c]:
            # 则交换
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
