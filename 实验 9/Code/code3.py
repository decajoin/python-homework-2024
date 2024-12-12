import jieba

s = '对于这么优秀的电影来说，再多的赞美都是多余的。'
s = s.replace('，', '').replace('。', '')
words = jieba.lcut(s)
filtered_words = [word for word in words if not word.isspace()]
print("/ ".join(filtered_words))
print(f"中文词语数是：{len(filtered_words)}")
