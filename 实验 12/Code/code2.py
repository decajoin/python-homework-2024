import re


def extract_numbers():
    filename = "data.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式提取所有数值
        numbers = re.findall(r'\d+', content)  # 匹配所有整数
        numbers = list(map(int, numbers))  # 将提取的数值转换为整数
        print(f"提取的数值：{numbers}")
        return numbers

    except FileNotFoundError:
        print(f"文件 {filename} 未找到，请检查文件路径。")


# 调用函数
numbers = extract_numbers()
# 计算总和和平均值
total = sum(numbers)
avg = total / len(numbers)
print(f"总和：{total}")
print(f"平均值：{avg:.2f}")
