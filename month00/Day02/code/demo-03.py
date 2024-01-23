"""
    序列赋值
        格式：
            变量名1, 变量名2 = 值1, 值2
        说明：
            1. 变量个数必须与右侧的值的个数相同
            2. 变量名按照位置上接受对应位置上值
"""
# 序列赋值
num1, num2 = 100, 200
print("num1 : ", num1, "  num2 : ", num2)

# 用途：变量交换
name01 = "张百万"
name02 = "李四"
print("name01: ", name01, " name02: ", name02)

name01, name02 = name02, name01
print("name01: ", name01, " name02: ", name02)



