"""

"""


def func01(p1, p2, p3):
    p1 = 100
    p2 = 200
    p3.append(300)
    return p1
#体会：函数内部修改传入的可变数据,无需通过return返回.
a = 10
b = [20]
c = [30]
d = func01(a,b,c)
print(a) # ?
print(b) # ?
print(c) # ?
print(d) # ?
