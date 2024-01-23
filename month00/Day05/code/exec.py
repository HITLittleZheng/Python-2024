"""
    一个小球从高度为100米落下, 每次弹回原高度的一半。
    计算:
        总共经过了多少米? 最终落地(最小弹起高度0.01米)
"""

height = 100

distance = height
count = 0
while height / 2 > 0.01:
    height /= 2
    count += 1
    print("第" + str(count) + '次的高度为' + str(height))
    distance += height * 2

print("共经过： ", count, '次', distance, "米")
