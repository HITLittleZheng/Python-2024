"""
ftp文件服务器服务端
"""
import os
from threading import Thread
from socket import *
from time import sleep

# 文件库位置
FTP = "/home/tarena/FTP/"


# 自定义线程类做事情
class Handle(Thread):
    def __init__(self, conn):
        self.conn = conn
        super().__init__()

    # 具体干事
    def run(self):
        # 总分
        while True:
            request = self.conn.recv(1024)
            tmp = request.decode().split(' ')
            # 根据请求分情况讨论
            if not request or tmp[0] == "QUIT":
                break
            elif tmp[0] == "LIST":
                self.do_list()
            elif tmp[0] == "GET":
                self.do_get(tmp[1])  # tmp [GET,filename]
            elif tmp[0] == "PUT":
                self.do_put(tmp[1])  # [PUT,filename]
        self.conn.close()

    def do_list(self):
        files = os.listdir(FTP)  # 获取文件列表
        if files:
            self.conn.send(b"OK")
            sleep(0.1)  # 延迟发送
            data = "\n".join(files)
            self.conn.send(data.encode())
        else:
            self.conn.send(b"EMPTY")

    # 发送文件
    def do_get(self, filename):
        try:
            fr = open(FTP + filename, 'rb')
        except:
            self.conn.send(b"FAIL")
        else:
            self.conn.send(b"OK")
            sleep(0.1)
            while True:
                data = fr.read(1024)
                if not data:
                    break
                self.conn.send(data)
            fr.close()
            sleep(0.1)
            self.conn.send(b"##")

    # 　上传文件　：　接收文件
    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            self.conn.send(b"EXISTS")
        else:
            self.conn.send(b"OK")
            fw = open(FTP + filename, 'wb')
            while True:
                data = self.conn.recv(1024)
                if data == b"##":
                    break
                fw.write(data)
            fw.close()


# 　网络服务
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
