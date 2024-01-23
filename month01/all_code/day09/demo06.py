"""
    函数参数
        实际参数
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 适用性：当调用函数不能确定实参,
# 需要由第三方构建容器决定数据时.

# 序列实参：拆序列,传元素,按顺序对应
list01 = [10, 20, 30]
tuple01 = (10, 20, 30)
name = "孙悟空"
func01(*list01)
func01(*tuple01)
func01(*name)

# 字典实参：拆字典,传元素,按名称对应
dict01 = {"p2": 2, "p1": 1, "p3": 3}
func01(**dict01)
