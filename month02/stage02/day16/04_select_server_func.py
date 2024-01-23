"""
基于　ｓｅｌｅｃｔ 方法的ＩＯ网络并发
"""
from socket import *
from select import select

# 　服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 　ＩＯ监控列表
rlist = []


# 　创建监听套接字
def create_socket():
    sock = socket()
    sock.bind(ADDR)
    sock.setblocking(False)  # 配合非阻塞，防止系统网络产生的延迟
    return sock


# 处理客户端连接
def connect(sock):
    # 　处理连接
    conn, addr = sock.accept()
    print("Connect from", addr)
    conn.setblocking(False)
    rlist.append(conn)  # 添加关注


def handle(conn):
    # 　与客户端交互
    data = conn.recv(1024)
    if data:
        print("收到:", data.decode())
        conn.send(b'Thanks')
    else:
        rlist.remove(conn)  # 客户端退出
        conn.close()


def main():
    sock = create_socket()
    sock.listen(5)
    print("Listen the port %d" % PORT)
    while True:
        rs, ws, xs = select(rlist, [], [])
        for r in rs:
            if r == sock:
                connect(r)
            else:
                handle(r)  # 处理客户端


if __name__ == '__main__':
    main()
