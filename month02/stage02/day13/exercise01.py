"""
练习：
1. 求100000以内质数之和，并且计算这个求和过程的时间

2. 将100000分成4份，创建4个进程，每个进程求
其中一份的质数之和，统计4个进程执行完的时间
"""
import time
from multiprocessing import Process

# 判断一个数字是否为质数
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num // 2 + 1):
        if num % i == 0:
            return False
    return True

class Prime(Process):
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

def process_10():
    jobs = []
    # 1  25001 50001 75001
    for i in range(1,100001,10000):
        p = Prime(i,i + 10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs] # 等4个进程结束

begin = time.time() # 时间戳
process_10() # 10个进程用时： 6.666069269180298
print("10个进程用时：",time.time() - begin)


################### 单个进程 ################
# def process_1():
#     prime = []  # 存放质数
#     for i in range(1,100001):
#         if is_prime(i):
#             prime.append(i)
#     print(sum(prime))
#
# begin = time.time() # 时间戳
# process_1() # 一个进程用时： 12.83949327468872
# print("一个进程用时：",time.time() - begin)




