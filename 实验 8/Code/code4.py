import jieba
# 打开文件
with open("论语-网络版.txt", "r", encoding="utf-8") as fi:
    content = fi.read()

# 统计字符频率
char_count = {}
for char in content:
    if char.strip():  # 排除空格和回车
        char_count[char] = char_count.get(char, 0) + 1

# 保存结果
with open("论语-汉字统计.txt", "w", encoding="utf-8") as fo:
    for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
        fo.write(f"{char}:{count}\n")

print("字符统计已完成，结果保存在'论语-汉字统计.txt'")

# 分词并统计词语频率
with open("论语-网络版.txt", "r", encoding="utf-8") as fi:
    content = fi.read()

words = jieba.cut(content)
word_count = {}
for word in words:
    if word.strip() and word.isalnum():  # 排除标点符号
        word_count[word] = word_count.get(word, 0) + 1

# 保存结果
with open("论语-词语统计.txt", "w", encoding="utf-8") as fo:
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        fo.write(f"{word}:{count}\n")

print("词语统计已完成，结果保存在'论语-词语统计.txt'")
