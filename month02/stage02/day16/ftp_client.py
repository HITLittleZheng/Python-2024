"""
ftp文件服务器客户端
"""
from socket import *
import sys

# 服务器地址
from time import sleep

SERVER_ADDR = ("127.0.0.1", 8888)


# 具体发起请求 逻辑
class Handle:
    def __init__(self):
        self.sock = self._connect()
        self.status = {
            "OK": "成功",
            "FAIL": "文件下载失败",
            "EXISTS": "文件已存在",
            "EMPTY": "文件库为空"
        }

    def _connect(self):
        sock = socket()
        sock.connect(SERVER_ADDR)
        return sock

    # 下载文件
    def do_get(self, filename):
        msg = "GET " + filename
        self.sock.send(msg.encode())  # 发请求
        response = self.sock.recv(128).decode()  # 收响应
        if response == 'OK':
            fw = open(filename, 'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                fw.write(data)
            fw.close()
        else:
            print(self.status[response])

    def do_quit(self):
        self.sock.send(b"QUIT")
        self.sock.close()
        sys.exit("谢谢使用")

    # 　请求文件列表
    def do_list(self):
        self.sock.send(b"LIST")  # 发请求
        response = self.sock.recv(128).decode()  # 收响应
        if response == 'OK':
            # 收文件列表
            data = self.sock.recv(1024 * 1024)
            print(data.decode())
        else:
            print(self.status[response])

    # 上传　发送文件
    def do_put(self, filename):
        try:
            fr = open(filename, 'rb')
        except:
            print(self.status["FAIL"])
            return
        filename = filename.split("/")[-1] # 提取文件名
        msg = "PUT " + filename
        self.sock.send(msg.encode())  # 发请求
        response = self.sock.recv(128).decode()  # 收响应
        if response == 'OK':
            while True:
                data = fr.read(1024)
                if not data:
                    break
                self.sock.send(data)
            fr.close()
            sleep(0.1)
            self.sock.send(b"##")
        else:
            print(self.status[response])


# 选择输入
class FTPView:
    def __init__(self):
        self.handle = Handle()

    def _menu(self):
        print("""
    ============== FTP SERVER ============= 
     1. 查看文件  2. 下载  3. 上传  4. 退出
    =======================================    
        """)

    def _select(self):
        cmd = input("请输入选项:")
        if cmd == "1":
            self.handle.do_list()
        elif cmd == "2":
            filename = input("要下载的文件:")
            self.handle.do_get(filename)
        elif cmd == "3":
            filename = input("要上传的文件:")
            self.handle.do_put(filename)
        elif cmd == "4":
            self.handle.do_quit()
        else:
            print("请输入正确选项！")

    # 入口
    def main(self):
        while True:
            self._menu()
            self._select()


if __name__ == '__main__':
    ftp = FTPView()
    ftp.main()
