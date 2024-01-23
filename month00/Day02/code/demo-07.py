"""
    类型转换
"""

# 1. float()
#   int --> float
print(float())  # 0.0
print(float(10))  # 10.0

#   str --> float
print(float('45'), type(float('45')))  # 45.0 <class 'float'>
print(float('4.5'), type(float('4.5')))  # 4.5 <class 'float'>

# 错误写法
# print(float(4+5j)) # 复数不能转为浮点类型
# print(float('5A')) # 字符A不能转为浮点型
# print(float("9-")) # -号在数字后侧不能转为浮点型


# int() 将数据对象转为整型
# str --> int
int01 = int('-10')
print(int01, type(int01))

# int02 = int('3.1415926') # 异常 不能将.转换为整数
# print(int02, type(int02))

# float --> int
int03 = int(3.1415926)
print(int03, type(int03))

# bool --> int
print(int(True), type(int(True)))  # 1
print(int(False))  # 0


# str 将数据对象转换为字符串类型
print(str(10), type(str(10)))
print(str(10.0), type(str(10.0)))
print(str(4+6j), type(str(4+6j)))
print(str(True), type(str(True)))

# bool 将数据对象转为bool类型
# 以下类型转换为bool类型为假 False
print(bool(''))
print(bool(0))
print(bool(0.0))
print(bool(None))