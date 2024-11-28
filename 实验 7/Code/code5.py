# 判断是否为回文数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 判断是否为素数（复用函数）
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 找出所有既是回文数又是素数的3位数
results = [n for n in range(100, 1000) if is_palindrome(n) and is_prime(n)]

# 输出结果
print(results)
