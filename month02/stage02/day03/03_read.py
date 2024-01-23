"""
文件读操作演示
1. open后每次读取都是从上次结束的位置继续读
2. 读取到文件结尾后，如果继续读返回值是空字串
"""

# 读方式打开文件
fr = open("file.txt","r")

# 二进制打开
# fr = open("file.txt","rb")

#　读取文件内容
data = fr.read()
print(data)

# 循环读取直到文件结尾停止
# while True:
#     data = fr.read(1)
#     if not data:
#         break # 当读取到结尾ｄａｔａ为空时结束循环
#     print(data,end="")

# 按照行读取
# line = fr.readline()
# print(line)
# line = fr.readline()
# print(line)

#　读取多行内容 (参数字符数到哪一行就读到哪一行)
# lines = fr.readlines(12)
# print(lines)

#　迭代每次取一行
# for line in fr:
#      print(line)

# 关闭
fr.close()
