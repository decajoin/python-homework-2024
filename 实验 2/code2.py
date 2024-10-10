# 实现埃拉托色尼筛法（埃筛）
import math

def sieve_of_eratosthenes(n):
    # 创建一个布尔数组，初始全为True，表示所有数都是素数
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        # 如果 primes[p] 未被标记为False，则它是素数
        if primes[p] == True:
            # 标记所有p的倍数为False
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    # 将所有素数存入列表
    prime_numbers = []
    for p in range(2, n):
        if primes[p]:
            prime_numbers.append(p)

    return prime_numbers

# 输入一个大于2的自然数
n = int(input("请输入一个大于2的自然数："))

# 调用函数获取素数列表
if n > 2:
    prime_list = sieve_of_eratosthenes(n)
    print("小于", n, "的所有素数是：")
    print(prime_list)
else:
    print("请输入一个大于2的自然数。")
