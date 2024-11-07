# 初始化计数器，用于控制每行输出的数字个数
count = 0

# 遍历 10 到 50 之间的所有数
for num in range(10, 51):
    # 检查是否为 3 的倍数
    if num % 3 == 0:
        print(num, end=" ")
        count += 1
        # 每输出 5 个数，换行一次
        if count % 5 == 0:
            print()

# 输出格式上的调整，如果最后一行不足 5 个数，自动换行
if count % 5 != 0:
    print()
