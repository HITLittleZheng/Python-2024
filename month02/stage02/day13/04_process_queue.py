"""
进程间通信 ： 消息队列
"""
from multiprocessing import Process,Queue

q = Queue() # 消息队列

# 子进程 : 根据父进程指令做事
def handle():
    while True:
        cmd = q.get() # 获取指令
        if cmd == "+":
            print("执行加法操作")
        elif cmd == "-":
            print("执行减法操作")


def main():
    while True:
        cmd = input("指令：")
        if cmd == "#":
            break
        q.put(cmd) # 存入指令

# 创建子进程
p = Process(target=handle,daemon=True)
p.start()
main()
