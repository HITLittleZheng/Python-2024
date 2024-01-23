"""
写操作示例
1.每次写操作都会继续上次的内容往下写
2.每次写操作不会自动添加任何格式
"""

# 写操作打开
# fw = open("file.txt","w")

# 二进制方式
# fw = open("file.txt","wb")

# 追加方式
fw = open("file.txt","ab")

# 写入内容
n = fw.write("Hello,死鬼\n".encode())
print(n) # 写入的字符个数或者字节数
fw.write("哎呀,干啥\n".encode())

# 将列表每一项分别写入
# data = ["Python web\n","爬虫\n","机器学习\n","数据分析"]
# fw.writelines(data)


fw.close()
