# 定义函数判断是否为素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 输入两个整数
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

# 统计范围内的素数个数
prime_count = sum(1 for i in range(min(x, y), max(x, y) + 1) if is_prime(i))

# 输出结果
print(f"Number of primes between {x} and {y}: {prime_count}")
