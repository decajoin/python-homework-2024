def my_fun(n):
    sum_val = 0
    for i in range(1, n + 1):
        sum_val += i / (2 * i - 1)
    return sum_val

n = int(input("请输入n的值："))
print("级数的结果为：", my_fun(n))
