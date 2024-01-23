"""
ftp文件服务器服务端
"""
from threading import Thread
from socket import *


# 自定义线程类做事情
class Handle(Thread):
    def __init__(self, conn):
        self.conn = conn
        super().__init__()

    # 　具体干事
    def run(self):
        # 总分
        while True:
            request = self.conn.recv(1024)
            # 根据请求分情况讨论
            if request == "LIST":
                self.do_list()
            elif request == "GET":
                self.do_get()
        self.conn.close()

    def do_list(self):
        pass

    def do_get(self):
        pass

#　网络服务
class FTPServer:
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self._create_socket()

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    # 启动服务
    def serve_forever(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            conn, addr = self.sock.accept()
            print("Connect from", addr)
            # 　为客户端生成一个线程
            handle = Handle(conn)
            handle.start()


if __name__ == '__main__':
    ftp = FTPServer(host="0.0.0.0", port=8888)
    ftp.serve_forever()  # 启动服务
