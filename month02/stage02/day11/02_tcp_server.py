"""
tcp服务端流程
重点代码
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听
tcp_socket.listen(3)

# 处理客户端连接
while True:
    print("等待连接 ...")
    conn,addr = tcp_socket.accept()
    print("连接了：",addr)
    # 循环收发数据
    while True:
        data = conn.recv(5)
        # 无论断开还是收到##都表示客户端结束
        if not data or data == b"##":
            break
        print("收到:",data.decode()) # data->bytes
        conn.send(b'Thanks')
    conn.close() # 断开连接

tcp_socket.close() # 不能连接新的客户端




