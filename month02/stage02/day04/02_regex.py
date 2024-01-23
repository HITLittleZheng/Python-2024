"""
正则表达式学习 示例  02_regex.py
"""
import re

# 普通字符
# result = re.findall("ab","abcdabcdefa")
# print(result)

# . 匹配任意一个字符 除了换行
# result = re.findall('张.丰',"张三丰,张四丰,张五丰")
# print(result)

# 匹配字符集中的任意一个字符
# result = re.findall('[ !A-Z]',"How are you!")
# print(result)
#
# result = re.findall('[^ !A-Z]',"How are you!")
# print(result)

# 匹配o出现0次或者多次的情况
# result = re.findall('wo*',"wooooo~~w!")
# print(result)
#
# # 匹配o出现1次或者多次的情况
# result = re.findall('wo+',"wooooo~~w!")
# print(result)
#
# # 匹配o出现0次或者1次的情况
# result = re.findall('wo?',"wooooo~~w!")
# print(result)
#
# # 匹配指定次数或区间: {3} {2,4} {3,} {,4}
# result = re.findall('wo{3,}',"wooooo~~w!")
# print(result)

# 匹配字符串开头和结尾位置
# result = re.findall('^Jame',"hi,Jame")
# print(result)
#
# result = re.findall('Jame$',"hi,Jame.")
# print(result)

# 匹配任意数字字符 \d == [0-9]
# result = re.findall('\d{1,5}',"Mysql: 3306, http:80")
# print(result)
#
# result = re.findall('\D+',"Mysql: 3306, http:80")
# print(result)

# 匹配普通字符和非普通字符
# result = re.findall('\w+',"server_port = 四个八")
# print(result)
#
# result = re.findall('\W+',"server_port = 8888")
# print(result)

# 匹配空字符
# result = re.findall('\w+\s+\w+',"匹配：hello    world")
# print(result)
#
# result = re.findall('\S+',"匹配：hello    world")
# print(result)


# 匹配单词边界和非单词边界
# result = re.findall(r'\bis',"This is a test.")
# print(result)
#
# result = re.findall(r'\Bis',"This is a test.")
# print(result)

# 或匹配
# result = re.findall(r'\b\w{2}\b|\b\w{4}\b',"This is are test.")
# print(result)

# 元字符字符匹配时使用 \表示匹配自身 \.->.
# result = re.findall('-?\d+\.?\d*',"15 -3.6 5.24 -45")
# print(result)


# 贪婪 --》 非贪婪  + --》 +?
# result = re.findall('a.+?c',"abbbcbbbc")
# print(result)



# 当正则表达式没有子组的时候，返回值列表
# 每项为匹配到的内容，当有子组时返回值列表
# 每项为子组所对应的部分内容
# info = "Lily:1999  Tom:2000"
# result = re.findall('(\w+):(\d+)',info)
# print(result)

# 匹配ab重复
# result = re.search('(ab)+',"ababababab")
# print(result.group()) # 获取匹配结果

# 给子组起名字
# result = re.search('(?P<xing>王|李)\w{1,3}',"王者荣耀")
# print(result.group())