def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

def my_fun():
    sum_val = 0
    n = int(input("请输入n的值："))
    for i in range(1, n + 1):
        sum_val += fac(i) ** 3

    print("结果是：{}".format(sum_val))

my_fun()
