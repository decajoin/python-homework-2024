# 输入行数
n = int(input("输入行数："))

# 遍历每一行
for i in range(1, n + 1):
    # 打印空格
    print(" " * 2 * (n - i), end="")

    # 打印递减数字
    for j in range(i, 0, -1):
        print(j, end=" ")

    # 打印递增数字
    for j in range(2, i + 1):
        print(j, end=" ")

    # 换行
    print()
