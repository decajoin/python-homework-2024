k, n = eval(input("请输入k，n的值: "))

s = 0
item = 0
for i in range(1, n + 1):
    item = item * 10 + k  # 将当前项的数字累加起来
    s += item
print("值为：", s)
