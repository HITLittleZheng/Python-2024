"""
    基本数据类型
        字符串类型：
        整型：
        复数型: 实部 + 虚部 组成的数

        type(): 查看对应的数据类型

"""
# 字符串
str01 = '单引号'
str02 = "双引号"
print(str01, type(str01))
print(str02, type(str02))

# 三引号：所见即所得 可以换行
str03 = '''三
    单
        引
            号'''
print(str03, type(str03))

name = "我是：'严航'"
name = '我是："严航"'
print(name)

# 字符串转义
# r'' 声明原是字符串 不要将\n转换为换行 ...
path = r'C:\BJTT\Desktop\node\t训练营\Day02'
print(path)

# 整型
num1 = 10
num2 = -20
print(num1, type(num1))  # <class 'int'>
print(num2, type(num2))  # <class 'int'>

# 浮点型
# 1. 小数方式
num3 = 30.0
print(num3, type(num3))  # <class 'float'>

# 2. 科学计数法
# 小数|整数e|E[-]指数
# 作用：小数或整数乘以10的指数次方
num4 = 3.14E5
# num4 = 3.14e-2
print(num4, type(num4))

# 复数
num5 = 3.4 + 5J
print(num5, type(num5))  # <class 'complex'>


# 布尔型
print(True, type(True))
print(False, type(False))

# None 空值对象
# 占位
age = None
print(age, type(age))
age = 18
print(age, type(age))
# 解除绑定关系
age = None
print(age, type(age))

