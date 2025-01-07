import re

def quote_ratio():
    filename = "笑傲江湖.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        total_chars = len(text)
        # 提取引号内的字符
        quotes = re.findall(r'“(.*?)”', text)
        quote_chars = sum(len(quote) for quote in quotes)
        ratio = (quote_chars / total_chars) * 100
        print(f"占总字符比例：{ratio:.2f}%")
    except FileNotFoundError:
        print(f"文件 {filename} 未找到，请检查文件路径。")

quote_ratio()
