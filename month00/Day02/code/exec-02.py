"""
    计算加速度
        加速度 = (距离 - 初速度 * 时间) * 2 / 时间 ** 2
"""
# 1. 获取数据
distance = float(input("请输入距离："))
init_speed = float(input("请输入初速度："))
times = float(input("请输入时间："))

# 2. 逻辑计算
acc_speed = (distance - init_speed * times) * 2 / times ** 2

# 3. 显示结果
# 注意：
#       + 在字符串和字符串中表示拼接；
#       在数值中操作表示相加; 如果字符串 + 数值型则出发异常 TypeError
#       所以对于acc_speed转为字符串类型
print("加速度为：" + str(acc_speed))

# round(数值, 小数需要保留的位置) --> 四舍五入
# print() 中 逗号表示的是需要打印的多个值 无需注意各个值的类型
print("加速度： ", round(acc_speed, 2))