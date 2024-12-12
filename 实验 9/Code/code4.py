from collections import Counter

with open("天龙八部-网络版.txt", "r", encoding="utf-8") as f:
    text = f.read()

counter = Counter(text)
most_common = counter.most_common(100)

with open("天龙八部-字符统计.txt", "w", encoding="utf-8") as f:
    for char, count in most_common:
        f.write(f"{char}:{count}\n")
