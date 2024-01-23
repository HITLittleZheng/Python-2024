"""
with 语句
"""

# 打开文件生成文件对象 --> fr只能在with语句块中使用
with open("file.txt") as fr:
    data = fr.read()
    print(data)

# fr自动销毁 无需 close


