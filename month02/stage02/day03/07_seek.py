"""
文件偏移量操作
"""

file = open("file.txt","wb+")

file.write("世界和平".encode())
file.flush()

print("文件偏移量:",file.tell()) # 文件偏移量大小

# 1 2为基准必须 二进制打开
file.seek(-6,2)

file.write("向".encode()) # 覆盖内容

# data = file.read()
# print("内容:",data.decode())

file.close()