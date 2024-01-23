"""
正则表达式练习
"""
import re

# 匹配出大写字母开头的单词
# result = re.findall('[A-Z][a-z]*',"I am Tom")
# print(result)
#
# # 匹配出所有数字
# result = re.findall('[0-9]+',"2021-11-30")
# print(result)
#
# # 匹配出所有数字
# result = re.findall('-?[0-9]+',"-18度，23岁小战士站岗2小时")
# print(result)
#
#
# # 匹配下手机号码
# result = re.findall('1[3-9][0-9]{9}',"王总：15840665987")
# print(result)
#
# # 匹配QQ号码
# result = re.findall('[1-9][0-9]{5,10}',"王总QQ：125664458")
# print(result)

# 输入一个user，通过正则表达式验证输入的内容
# 是否只有6-10位数字字母下划线构成
# user = input("User:")
# result = re.findall('^[_0-9a-zA-Z]{6,10}$',user)
# print(result)


# 匹配下手机号码
# result = re.findall(r'\b1[3-9][0-9]{9}\b',"王总：15840665987,卡号：6933615866854235568")
# print(result)


# 匹配薪资
# result = re.findall('\$\d+',"小王日薪:$240")
# print(result)


# 匹配书名
# books = "《老人 && 海》，《我的祖国 ！！》，《小王子，wow 》，《妖精 —— 放开爷爷》"
# result = re.findall('《.+?》',books)
# print(result)

# 匹配李刚的出生年份
# info = "王刚：1996年出生，李刚：1997年出生，刘刚：1997年出生"
# result = re.findall('李刚：(\d{4})',info)
# print(result)

# 匹配 IP地址 每个部分1-3位数字 共4组
# result = re.search("(\d{1,3}\.?){4}","IP: 192.168.5.16")
# print(result.group())


result = re.search("[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+","Levi: lvze@tedu.cn")
print(result.group())



