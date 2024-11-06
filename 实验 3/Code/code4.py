# 获取输入的单词数量
n = int(input("请输入单词数量 n: "))

# 初始化字典来存储单词及其译文
dictionary = {}

# 逐行输入 n 个单词及其译文
for _ in range(n):
    english_word, translation = input().split()
    dictionary[english_word] = translation

# 输入要查询的单词
query_word = input("请输入要查询的单词: ")

# 查询单词并输出结果
if query_word in dictionary:
    print(dictionary[query_word])
else:
    print("not found")
