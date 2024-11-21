def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 主程序调用
num = int(input("请输入一个整数："))
if is_prime(num):
    print(f"{num} 是素数")
else:
    print(f"{num} 不是素数")
