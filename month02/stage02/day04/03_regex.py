"""
re模块小函数
"""
import re

# 利用正则表达式分割目标字符串 返回列表
# info = "张三   李四     王五   赵柳"
# print(re.split("\s+",info))

# 使用/替换正则表达式匹配到的部分，返回新字符串
# info = "张三   李四      王五  赵柳"
# print(re.sub("\s+","/",info))


# 匹配第一处符合正则规则的内容 info[0:2]
# info = "  张三   李四      王五  赵柳"
# result = re.search("\w+",info)
# print(result.group()) # 获取匹配内容
# print(result.span()) # 获取匹配内容对应的位置

# 匹配目标字符串开头位置
info = "张三:1998   王五:1999"
result = re.match("(\w+):(?P<year>\d+)",info)
print(result.group())
print(result.group(1)) # 只获取第一组内容
print(result.group("year")) # 只获取year组内容

# 匹配所有符合条件的内容。返回迭代对象
# info = "张三   李四      王五  赵柳"
# result = re.finditer("\w+",info)
# for item in result:
#     print(item.group()) # 每次取出一个匹配对象
