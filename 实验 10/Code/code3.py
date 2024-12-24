# 读取两个CSV文件并找相同字符
import csv

file1 = '命运-字符统计.csv'
file2 = '寻梦-字符统计.csv'
output_common = '相同字符.txt'

def read_csv(file):
    with open(file, 'r', encoding='utf-8') as f:
        return set(row[0] for row in csv.reader(f))

chars1 = read_csv(file1)
chars2 = read_csv(file2)

# 找相同字符并保存到文件
common_chars = chars1 & chars2
with open(output_common, 'w', encoding='utf-8') as f:
    f.write(','.join(common_chars))

print("任务2.2完成：相同字符已保存到相同字符.txt 文件！")
