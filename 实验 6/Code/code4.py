import random

# 定义奖项和对应概率范围
reward = {'一等奖': (0, 0.1), '二等奖': (0.1, 0.3), '三等奖': (0.3, 0.6), '谢谢您': (0.6, 1)}

def rewardFun():
    rand_num = random.random()
    for prize, (start, end) in reward.items():
        if start <= rand_num < end:
            return prize

# 模拟500次抽奖，统计获奖结果
results = {'一等奖': 0, '二等奖': 0, '三等奖': 0, '谢谢您': 0}
for _ in range(500):
    prize = rewardFun()
    results[prize] += 1

print("抽奖结果统计：")
for prize, count in results.items():
    print(f"{prize}: {count}次")
