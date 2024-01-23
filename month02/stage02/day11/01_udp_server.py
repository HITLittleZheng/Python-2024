"""
udp 服务端流程示例
udp套接字可以发送空子串
"""
from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0",8888))


# 循环先收后发
while True:
    data,addr = udp_socket.recvfrom(5)
    if data == b"##":
        break
    print(addr,":",data.decode()) # data->byte
    udp_socket.sendto(b"Thanks",addr) # addr回复

# 关闭套接字
udp_socket.close()






