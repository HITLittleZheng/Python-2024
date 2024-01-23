"""
基于 线程的网络并发模型
重点代码
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
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            print(data.decode())
            self.conn.send(b"Test")
        self.conn.close()


#　网络服务
class TCPServer:
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
    server = TCPServer(host="0.0.0.0", port=8888)
    server.serve_forever()  # 启动服务
