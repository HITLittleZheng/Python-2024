"""
tcp服务端流程
重点代码
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8880))

# 设置监听
tcp_socket.listen(3)

# 处理客户端连接
print("服务启动 ...")
while True:
    conn,addr = tcp_socket.accept() # 连接
    data = conn.recv(5)
    print(addr,":",data.decode())
    conn.send(b'Thanks')
    conn.close() # 断开连接

tcp_socket.close() # 不能连接新的客户端




