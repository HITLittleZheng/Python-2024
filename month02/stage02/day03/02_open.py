"""
打开文件
"""

# 读方式打开文件 文件必须存在
file = open("../day02/2.txt","r")
print(file)

# 写方式打开文件  文件不存在创建存在情况
# file = open("file.txt","w")
# print(file)

# 追加,文件存在不会清空原来内容
# file = open("file.txt","a")
# print(file)

# 读写文件

# 关闭操作
file.close()