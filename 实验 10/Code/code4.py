import csv

# 读取星座数据
def load_sun_signs(file):
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        return {row[0]: (row[1], row[2], chr(int(row[3]))) for row in reader}

sun_signs = load_sun_signs('SunSign.csv')

# 循环获取用户输入
while True:
    user_input = input("请输入星座名称（输入 'exit' 退出）：")
    if user_input.lower() == 'exit':
        break
    elif user_input in sun_signs:
        start_date, end_date, unicode_char = sun_signs[user_input]
        print(f"{user_input}：出生日期范围 {start_date} 至 {end_date}，对应字符 {unicode_char}")
    else:
        print("输入星座名称有误！")
