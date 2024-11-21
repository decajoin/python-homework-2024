def sum_even_series(n):
    sum_val = 0
    for i in range(2, n + 1, 2):
        sum_val += 1 / (i ** 2)
    return sum_val

def sum_odd_series(n):
    sum_val = 0
    for i in range(1, n + 1, 2):
        sum_val += 1 / (i ** 2)
    return sum_val

def calculate_series(n):
    if n % 2 == 0:
        return sum_even_series(n)
    else:
        return sum_odd_series(n)

# 输入并计算
n = int(input("请输入一个正整数："))
result = calculate_series(n)
print("结果是：", result)
