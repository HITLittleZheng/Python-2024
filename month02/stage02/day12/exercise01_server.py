"""
练习1 服务端
"""
from socket import *

chat = {
    "几岁": "我两岁啦",
    "你好": "你好啊",
    "男生女生": "我机器人啦",
    "叫什么": "我叫小美"
}


# 找答案
def xiaomei(q):
    for key, value in chat.items():
        if key in q:
            return value
    return "人家还小，不知道啦"


def main():
    # 创建监听套接字
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0", 8888))
    tcp_socket.listen(3)

    print("服务启动 ...")
    while True:
        conn, addr = tcp_socket.accept()  # 连接
        q = conn.recv(1024).decode()
        data = xiaomei(q)  # 找答案
        conn.send(data.encode())
        conn.close()  # 断开连接


if __name__ == '__main__':
    main()
