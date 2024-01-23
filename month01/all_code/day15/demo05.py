"""
    标准库模块
        time 时间模块
"""
import time

# 人类时间:2021年11月18日 16:32:25
# -- 时间元组(年,月,日,时,分,秒,星期,年的第几天,夏令时)
time_tuple = time.localtime()
print(time_tuple[0])  # 年
print(time_tuple[6])  # 星期
print(time_tuple[-3])  # 星期
print(time_tuple[:3])  # 年月日
print(time_tuple[3:6])  # 时分秒

# 机器时间
# -- 时间戳:从1970年到现在经过的秒数
print(time.time())  # 1637224879.6712253

# 时间元组 <--> 时间戳
# 语法:时间戳 = time.mktime(时间元组)
print(time.mktime(time_tuple))
# 语法:时间元组 = time.localtime(时间戳)
print(time.localtime(1637224879.6712253))

# 时间元组 <--> 字符串
# 语法：字符串 = time.strftime(格式,时间元组)
print(time.strftime("%y/%m/%d %H:%M:%S", time_tuple))
# 2021/11/18 16:51:49
print(time.strftime("%Y/%m/%d %H:%M:%S", time_tuple))
# 2021年11月18日 16时53分32秒　
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", time_tuple))
# 语法：时间元组 = time.strptime(字符串,格式)
print(time.strptime("2021年11月18日 16时53分32秒", "%Y年%m月%d日 %H时%M分%S秒"))
