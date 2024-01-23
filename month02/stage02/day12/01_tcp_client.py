"""
tcp 客户端流程
重点代码
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8880)

# 发送接受
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket = socket()
    tcp_socket.connect(ADDR) # 连接
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())
    tcp_socket.close() # 断开




