"""
    函数内存分布
"""
def func01(p1,p2):
    p1 = 10
    p2[0] = 20
    return 30

data01 = 1
data02 = [2]
data03 = func01(data01,data02)
print(data01)
print(data02)
print(data03)
