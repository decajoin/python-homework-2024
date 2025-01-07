import re
from collections import Counter

def count_words():
    filename = "笑傲江湖.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        # 提取中文字符
        words = re.findall(r'[\u4e00-\u9fff]', text)
        counter = Counter(words)
        # 输出出现次数最多的前5个词语
        top5 = counter.most_common(5)
        print({word: count for word, count in top5})
    except FileNotFoundError:
        print(f"文件 {filename} 未找到，请检查文件路径。")

count_words()
