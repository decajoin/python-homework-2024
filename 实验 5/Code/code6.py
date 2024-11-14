# 获取用户输入的长字符串
input_string = input("请输入一段长字符串: ")

# 使用字典统计每个字符的出现次数
char_count = {}

# 遍历字符串并统计字符出现次数
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 找出最大出现次数
max_count = max(char_count.values())

# 找出所有出现次数等于最大次数的字符
max_chars = [char for char, count in char_count.items() if count == max_count]

# 输出结果
print(f"出现次数最多的字符是: {', '.join(max_chars)}，次数为: {max_count}")
