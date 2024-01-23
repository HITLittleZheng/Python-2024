"""
dict 客户端： 与用户交互发起请求
"""
from socket import *
import sys
import re

ADDR = ("127.0.0.1", 8888)  # 访问服务端


# 具体向服务端发送请求
class Handle:
    @staticmethod
    def check(info):
        if re.findall("^\w{6,}$",info):
            return True
        return False

    def __init__(self):
        self.sock = self._connect()

    def _connect(self):
        sock = socket()
        sock.connect(ADDR)
        return sock

    def do_exit(self):
        self.sock.send(b"E")
        self.sock.close()
        sys.exit("谢谢使用")

    # 　发起注册请求
    def do_register(self, name, passwd):
        if Handle.check(name) and Handle.check(passwd):
            request = "R\t%s\t%s" % (name, passwd)
            self.sock.send(request.encode())  # 发请求
            response = self.sock.recv(128)  # 收响应
            if response == b'T':
                print("注册成功")
            else:
                print("注册失败")
        else:
            print("名字或密码需为大于6位数字字母下划线")

    # 　发起登录请求
    def do_login(self, name, passwd):
        request = "L\t%s\t%s" % (name, passwd)
        self.sock.send(request.encode())  # 发请求
        response = self.sock.recv(128)  # 收响应
        if response == b'T':
            print("登录成功")
            return True
        else:
            print("登录失败")

    # 查询单词
    def do_query(self):
        while True:
            word = input("要查询的单词:")
            if not word or word == '##':
                break  # 结束查单词
            request = "Q\t" + word
            self.sock.send(request.encode())
            response = self.sock.recv(1024).decode()
            tmp = response.split("\t", 1)  # 根据协议分割
            if tmp[0] == 'T':
                print("%s : %s\n" % (word, tmp[1]))
            else:
                print("没有查到该单词\n")

    # 历史记录
    def do_hist(self):
        self.sock.send(b'H')
        response = self.sock.recv(1024).decode()
        tmp = response.split('\t')
        if tmp[0] == 'T':
            for row in tmp[1].split(";"):
                print(row)  # 根据协议解析
        else:
            print("您还没有查询记录")


# 　与用户交互
class DictView:
    def __init__(self):
        self.handle = Handle()

    def _menu_2(self):
        while True:
            print("""
        ============== Query =============
         1. 查单词   2. 历史记录   3. 注销
        ==================================
            """)
            cmd = input("请输入选项:")
            if cmd == "1":
                self.handle.do_query()
            elif cmd == "2":
                self.handle.do_hist()
            elif cmd == "3":
                break
            else:
                print("请输入正确选项！")

    def _menu_1(self):
        while True:
            print("""
        ========= Welcome ==========
         1. 登录   2. 注册   3. 退出
        ============================
            """)
            cmd = input("请输入选项:")
            if cmd == "1":
                name = input("User:")
                passwd = input("Password:")
                if self.handle.do_login(name, passwd):
                    self._menu_2()  # 进入登录状态
            elif cmd == "2":
                name = input("User:")
                passwd = input("Password:")
                self.handle.do_register(name, passwd)
            elif cmd == "3":
                self.handle.do_exit()
            else:
                print("请输入正确选项！")

    def main(self):
        self._menu_1()


if __name__ == '__main__':
    dict = DictView()
    dict.main()
