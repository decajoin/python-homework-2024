s = 0
while True:
    x = input("请输入一个数(输入 'end' 结束): ")
    if x.lower() == "end":
        break
    try:
        s += float(x)
    except ValueError:
        print("无效的输入,请输入数字。")
        continue

print("各数之和 = ", s)