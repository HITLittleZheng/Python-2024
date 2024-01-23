"""
    序列赋值
        引入：
            假设现有变量：
                number01 = 30
                number02 = 60
            通过程序实现变量交换：
                number01 = 60
                number02 = 30

"""
number01 = 30
number02 = 60
print("交换前的数字：")
print("number01：", number01)
print("number02：", number02)

temp = number01
number01 = number02
number02 = temp
print("交换后的数字：")
print("number01：", number01)
print("number02：", number02)

