"""
    函数参数
        形式参数
"""


# 默认形参：实参可选
# 注意：必须从右向左依次存在
def func01(p1=True, p2="", p3=0):
    print(p1)
    print(p2)
    print(p3)

# 位置形参:实参必填
def func02(p1):
    print(p1)

func02(1)

func01(False, "a", 10)
func01()

func01(p2="b")
func01(p3=10)
func01(p2="b", p3=10)
# func01(p1=False, p2="b", p3=10) # 没必要通过关键字实参传递全部数据
# func01(p1=False, p3=10) # p1没必要通过关键字实参传递
func01(False, p3=10)
# func01(False, p2="b")
func01(False, "b")
