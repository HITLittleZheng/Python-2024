"""
    1. 超市西瓜 13元/个
        问：
            拿100元 可以买几个西瓜, 找零多少?

    2. 获取用户输入的秒数, 计算是多少小时多少分钟多少秒?
"""
# 练习1： 买西瓜
# 1. 定义变量
money = 100
price = 13

# 2. 进行运算
number = 100 // 13
remain = 100 % 13
print(money, "可以购买 ", number, "个西瓜. 剩余", remain, "元")

# 练习2： 通过总秒数求小时分钟秒数
'''
    小时： 1小时 = 60 分钟
          1小时 = 60分钟 = 3600秒
    分钟： 1分钟 = 60秒
'''
# 1. 获取数据
total_seo = int(input("请输入秒数："))

# 2. 逻辑计算
hour = total_seo // 3600
minute = total_seo % 3600 // 60
second = total_seo % 60

# 3. 打印输出
print(total_seo, "秒是: ", hour, "小时", minute, "分钟", second, "秒")
