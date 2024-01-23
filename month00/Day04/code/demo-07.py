"""
    注意
"""

# 1. 起始值和终止值相同, 则结果为空
for item in range(1, 1, 2):
    print(item)

# 2. 取值反向与步长方向不一致, 则结果为空
for item in range(5, 1):
    print(item)