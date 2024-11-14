# 获取用户输入的字符串
input_string = input("请输入一个字符串: ")

# 创建字典用于存储每个字符的出现次数
char_count = {}

# 遍历字符串，统计每个字符的出现次数
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 输出结果
print(f"字符串中有 {len(char_count)} 种字符，具体统计如下：")
for char, count in char_count.items():
    print(f"字符 '{char}' 出现了 {count} 次")
