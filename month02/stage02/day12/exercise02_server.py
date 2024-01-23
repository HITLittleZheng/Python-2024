"""
练习2 服务端
"""
from socket import *

# 监听套接字
sock = socket()
sock.bind(("0.0.0.0",8880))
sock.listen(5)

# 连接
conn,addr = sock.accept()
print("Connect from",addr)

while True:
    # 循环接收打印
    row = conn.recv(1024).decode()
    if row == "#":
        break
    print(row,end="")
print() # 换行

conn.close()
sock.close()
