def Fib(n):
    if n == 1 or n == 2:
        return 1
    return Fib(n - 1) + Fib(n - 2)

x = int(input("请输入 x 的值："))
print("F(" + str(x) + "): " + str(Fib(x)))
