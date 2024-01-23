"""
udp 客户端流程
"""
from socket import *

# 访问服务器使用的地址
ADDR = ("127.0.0.1",8888)

# udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)


# 循环输入内容发送
while True:
    msg = input(">>")
    udp_socket.sendto(msg.encode(),ADDR)
    if msg == "##":
        break # 退出标志
    data,addr = udp_socket.recvfrom(1024)
    print("From server:",data.decode())


udp_socket.close()
