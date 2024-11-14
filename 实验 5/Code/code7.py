# 定义敏感词列表
sensitive_words = ["枪支弹药", "借贷平台"]

# 获取用户输入的内容
user_input = input("请输入内容：")

# 遍历敏感词列表，替换内容
for word in sensitive_words:
    if word in user_input:  # 如果找到了敏感词
        user_input = user_input.replace(word, "***")

# 输出过滤后的内容
print("过滤后的内容：", user_input)
