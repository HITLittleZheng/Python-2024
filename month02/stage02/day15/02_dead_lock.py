"""
模拟死锁现象
"""
from time import sleep
from threading import Thread,Lock

# 银行账户
class Account:
    def __init__(self,id,balance,lock):
        self.id = id
        self.balance = balance
        self.lock =lock

    # 取钱
    def get(self,amount):
        self.balance -= amount

    # 存钱
    def put(self,amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

tom = Account("tom",80000,Lock())
abby = Account("abby",20000,Lock())

# from_ --> to  amount
def trans(from_,to,amount):
    from_.lock.acquire() # 上锁 from
    from_.get(amount) # 钱减少
    from_.lock.release() # 不会死锁

    sleep(0.1)
    to.lock.acquire() # 上锁 to
    to.put(amount)# 钱增加
    # from_.lock.release() # 会死锁
    to.lock.release()

if __name__ == '__main__':
    t1 = Thread(target=trans,args=(tom,abby,10000))
    t2 = Thread(target=trans,args=(abby,tom,10000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Tom:",tom.getBalance())
    print("Abby:",abby.getBalance())





