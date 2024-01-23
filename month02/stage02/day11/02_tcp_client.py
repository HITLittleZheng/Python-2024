"""
tcp 客户端流程
重点代码
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

# 默认值就是tcp套接字
tcp_socket = socket()

# 发起连接
tcp_socket.connect(ADDR)

# 发送接受
while True:
    msg = input(">>")
    tcp_socket.send(msg.encode())
    if not msg or msg == "##":
        break # 结束标志
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())

# 关闭
tcp_socket.close()




