import random
from collections import Counter

# Step 1: 创建一个包含随机数的文件 data.txt
with open('data.txt', 'w') as f:
    for _ in range(100):  # 生成100个1~100之间的随机整数
        f.write(f"{random.randint(1, 100)}\n")

# Step 2: 读取文件并统计出现次数
with open('data.txt', 'r') as f:
    numbers = list(map(int, f.readlines()))

# 统计数字出现的次数
counter = Counter(numbers)

# 找出出现次数最多的前5个数字
most_common_numbers = counter.most_common(5)

# Step 3: 将结果写入 most.txt 文件
with open('most.txt', 'w') as f:
    for number, count in most_common_numbers:
        f.write(f"{number}: {count}\n")

print("任务1完成：data.txt 和 most.txt 已生成！")
