def student_directory():
    print("学生通讯录管理系统")
    print("1. 显示所有信息")
    print("2. 追加信息")
    print("3. 删除信息")
    while True:
        choice = input("请输入数字1-3选择功能：")
        if choice in ['1', '2', '3']:
            print(f"您选择了功能{choice}.")
            return int(choice)
        else:
            print("输入错误，请重新输入数字1-3。")

def display_all(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"文件 {filename} 未找到，请检查文件路径。")

def append_info(filename, new_filename):
    student_info = input("请输入学生信息（格式：学号,姓名,电话号码,地址）：")
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(student_info + '\n')
    print("信息追加成功！")
    # 写入 new_address.txt
    with open(new_filename, 'a', encoding='utf-8') as new_file:
        new_file.write(student_info + '\n')
    # 显示追加后的信息
    display_all(filename)

def delete_info(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for index, line in enumerate(lines, start=1):
            print(f"{index}. {line.strip()}")
        to_delete = int(input("请输入要删除的行号："))
        if 1 <= to_delete <= len(lines):
            del lines[to_delete - 1]
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print("删除成功！")
        else:
            print("输入的行号无效！")
    except FileNotFoundError:
        print(f"文件 {filename} 未找到，请检查文件路径。")

# 主程序
filename = "address.txt"
new_filename = "new_address.txt"

while True:
    choice = student_directory()
    if choice == 1:
        display_all(filename)
    elif choice == 2:
        append_info(filename, new_filename)
    elif choice == 3:
        delete_info(filename)
