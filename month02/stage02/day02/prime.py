"""
函数: 判断一个数是否为质数
"""
def prime(num):
    if num <= 1:
        return False
    for i in range(2,num // 2 + 1):
        if num % i == 0:
            return False
    return True 

print(prime(12))

