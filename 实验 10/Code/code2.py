import csv
from collections import Counter

# 文件路径
file_paths = ['命运-网络版.txt', '寻梦-网络版.txt']
output_files = ['命运-字符统计.csv', '寻梦-字符统计.csv']

for i, file_path in enumerate(file_paths):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', '')  # 去除回车字符
    counter = Counter(text)
    most_common_chars = counter.most_common(100)  # 前100个字符

    # 保存到CSV文件
    with open(output_files[i], 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for char, count in most_common_chars:
            writer.writerow([char, count])

print("任务2.1完成：字符统计已保存到CSV文件！")
