"""
基于 Process 的tcp网络并发
重点代码 ！
"""
import sys
from socket import *
from multiprocessing import Process

# 服务器端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


# 处理客户端事务
def handle(conn, address=("", 0)):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        conn.send(b"Test")
    conn.close()


# 启动服务的主函数
def main():
    # 创建tcp监听套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %d" % PORT)
    # 循环连接客户端
    while True:
        try:
            conn, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sock.close()
            sys.exit("服务结束")
        # 为客户端开辟一个进程
        p = Process(target=handle, kwargs={"conn": conn, "address": addr})
        p.start()  # 启动进程


if __name__ == '__main__':
    main()
