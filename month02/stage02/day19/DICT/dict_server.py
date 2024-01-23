"""
接收请求，逻辑处理，发送响应
"""
from multiprocessing import Process
from socket import *
from dict_db import *


# 进程类做事情
class Handle(Process):
    def __init__(self, conn):
        self.conn = conn
        self.name = ""  # 记录登录状态
        self.db = Dict()  # 得到数据库处理对象
        super().__init__()

    # 　循环接收请求，分情况讨论
    def run(self):
        while True:
            request = self.conn.recv(1024)
            tmp = request.decode().split("\t")
            if not request or tmp[0] == 'E':
                break  # 客户端退出
            elif tmp[0] == 'R':
                # [R,name,passwd]
                self.do_register(tmp[1], tmp[2])
            elif tmp[0] == 'L':
                # [L,name,passwd]
                self.do_login(tmp[1], tmp[2])
            elif tmp[0] == 'Q':
                # [Q,word]
                self.do_query(tmp[1])
            elif tmp[0] == 'H':
                # [H]
                self.do_hist()

        self.db.close()
        self.conn.close()

    def do_hist(self):
        # ((name,word,time),....)
        data = self.db.hist(self.name)
        if data:
            res = "T\t"
            for row in data:
                res += "%s,%s,%s;" % row
            self.conn.send(res.encode())
        else:
            self.conn.send(b'F')

    # 查询单词
    def do_query(self, word):
        # (mean,) None
        mean = self.db.query(word)
        if mean:
            res = "T\t" + mean[0]
            self.conn.send(res.encode())
            self.db.insert_hist(self.name, word)  # 历史记录
        else:
            self.conn.send(b'F')

    def do_register(self, name, passwd):
        # 　数据库操作
        if self.db.register(name, passwd):
            self.conn.send(b'T')
        else:
            self.conn.send(b'F')

    def do_login(self, name, passwd):
        # 　数据库操作
        if self.db.login(name, passwd):
            self.conn.send(b'T')
            self.name = name  # 改为name实例变量记录登录状态
        else:
            self.conn.send(b'F')


# 　网络服务
class DictServer:
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
            # 　为客户端生成一个进程
            handle = Handle(conn)
            handle.start()


if __name__ == '__main__':
    dict = DictServer(host="0.0.0.0", port=8888)
    dict.serve_forever()  # 启动服务
