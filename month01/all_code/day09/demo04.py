"""
    函数参数
        形式参数
"""


# 星号元组形参：将多个位置实参合并为一个元组
def func01(*args):
    print(args)

# 双星号字典形参：将多个关键字实参合并为一个字典
def func02(**kwargs):
    print(kwargs)

func01(1)  # (1,)
func01()  # ()
func01(1, 2, 3)  # (1, 2, 3)
# func01(p=1) # 不支持关键字实参
func02(a=1, b=2)
# func02(1,2)# 不支持位置实参




