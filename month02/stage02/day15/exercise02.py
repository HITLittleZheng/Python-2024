"""
练习02：
创建2个分支线程，一个打印 1--52 这52个数字
一个打印 A--Z这26个字母，两个分支线程启动后
要求打印出来的顺序是 12A34B...5152Z
"""
from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock2.acquire()
        print(i)
        print(i + 1)
        lock1.release()

def print_chr():
    for i in range(65,91):
        lock1.acquire()
        print(chr(i))
        lock2.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_chr)

lock1.acquire() # 字母先锁住

t1.start()
t2.start()




