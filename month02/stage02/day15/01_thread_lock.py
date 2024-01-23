"""
线程互斥锁
"""
from threading import Lock,Thread

a = b = 1 #共享资源
lock = Lock()

def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()

t = Thread(target=value)
t.start()

while True:
    lock.acquire() # 上锁
    a += 1
    b += 1
    lock.release() # 解锁
