"""
    list --> str
"""
list01 = ["a", "b", "c"]  # 列表中元素必须是字符串
# 语法：字符串 = "连接符".join(列表)
result = "-".join(list01)
print(result)  # a-b-c
# 应用：
# 需求：根据某些逻辑循环拼接字符串
# 缺点：每次循环产生一个新字符串,存储当前,销毁之前
"""
result = ""
for number in range(10):  # 0~9
    # "" + "0"
    # "0" + "1"
    # "01" + "2"
    result += str(number)
print(result)
"""
# 解决:用可变数据代替不可变数据
result = []
for number in range(10):  # 0~9
    # 每次向同一个列表追加
    result.append(str(number))
# 列表(可变)->字符串(不可变)
result = "".join(result)
print(result)
#　练习：　
# 在终端中,循环录入字符串,如果录入空则停止.
# 停止录入后打印所有内容(一个字符串)
