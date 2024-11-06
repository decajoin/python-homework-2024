# (利用字典完成)输入字符串，输出字符串中出现次数最多的字母及其出现次数。
# 如果有多个字母出现次数一样，则按字符从小到大顺序输出字母及其出现次数。
# 如输入：aabbbcc,则输出c 3

# 输入字符串
input_str = input("请输入字符串：")

# 创建一个字典来记录每个字符的出现次数
char_count = {}

# 遍历字符串，统计每个字符的出现次数
for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 找到出现次数最多的字符
max_count = max(char_count.values())

# 按字符从小到大顺序输出所有出现次数最多的字符及其次数
max_chars = [char for char in sorted(char_count) if char_count[char] == max_count]
for char in max_chars:
    print(f"{char} {max_count}")
