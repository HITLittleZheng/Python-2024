"""
练习1 客户端
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

def chat(msg):
    tcp_socket = socket()
    tcp_socket.connect(ADDR)  # 连接
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    tcp_socket.close()  # 断开
    return data.decode() # 回复

def main():
    while True:
        msg = input("我:")
        if not msg:
            break
        print("小美:", chat(msg))

if __name__ == '__main__':
    main()



