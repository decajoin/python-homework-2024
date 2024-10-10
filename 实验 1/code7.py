# 输入一个字符串，输出其中出现次数最多的字符及出现的次数
def most_frequent_char(s):
    # 创建一个字典用于存储字符及其出现的次数
    char_count = {}

    # 遍历字符串，统计每个字符的出现次数
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # 初始化最大出现次数和对应字符
    max_count = 0
    max_char = ''

    # 遍历字典，找到出现次数最多的字符
    for key, value in char_count.items():
        if value > max_count:
            max_count = value
            max_char = key

    # 返回出现次数最多的字符及其出现的次数
    return max_char, max_count

# 测试
input_str = input("请输入一个字符串：")
char, count = most_frequent_char(input_str)
print("出现次数最多的字符是：", char)
print("出现的次数是：", count)
