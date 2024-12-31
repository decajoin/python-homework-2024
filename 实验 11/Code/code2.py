import jieba

# 读取文章内容
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# 统计“人”出现的次数
def count_word_frequency(article, word):
    words = jieba.cut(article)
    return sum(1 for w in words if w == word)

# 主程序
if __name__ == "__main__":
    article = read_article('../Docs/my_paper.txt')
    count = count_word_frequency(article, '人')
    with open('my_paperout.txt', 'w', encoding='utf-8') as f:
        f.write(f"“人”出现的次数：{count}")
