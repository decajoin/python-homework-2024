import random

# 生成一个 0 到 100 的随机整数
target_number = random.randint(0, 100)

# 初始化猜测变量
guess = -1

# 循环直到猜对为止
while guess != target_number:
    # 提示用户输入猜测的数字，并转换为整数
    guess = int(input("请输入你猜测的数字（0-100之间）: "))

    # 判断猜测结果
    if guess < target_number:
        print("小了，请继续")
    elif guess > target_number:
        print("大了，请继续")
    else:
        print("猜对了！")
