"""
线程GIL
"""
import time
from threading import Thread

# 判断一个数字是否为质数
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num // 2 + 1):
        if num % i == 0:
            return False
    return True

class Prime(Thread):
    """begin-end之间所有质数之和"""
    def __init__(self,begin,end):
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self):
        prime = []  # 存放质数
        for i in range(self.begin,self.end):
            if is_prime(i):
                prime.append(i)
        print(sum(prime))

def thread_10():
    jobs = []
    # 1  25001 50001 75001
    for i in range(1,100001,10000):
        t = Prime(i,i + 10000)
        jobs.append(t)
        t.start()
    [i.join() for i in jobs] # 等4个进程结束

begin = time.time() # 时间戳
thread_10()
print("10个线程用时：",time.time() - begin)


################### 单个进程 ################
# def process_1():
#     prime = []  # 存放质数
#     for i in range(1,100001):
#         if is_prime(i):
#             prime.append(i)
#     print(sum(prime))
#
# begin = time.time() # 时间戳
# process_1() #一个进程用时： 13.001709938049316
# print("一个进程用时：",time.time() - begin)




