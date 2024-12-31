import csv


# 读取学生名单
def read_student_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


# 读取考勤数据并找出缺勤学生
def find_absent_students(names, attendance_file):
    with open(attendance_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # 假设第一列是学生名字
        present_students = {row[0] for row in reader}

    absent_students = [name for name in names if name not in present_students]
    return absent_students


# 主程序
if __name__ == "__main__":
    names = read_student_names('../Docs/Name.txt')
    absent = find_absent_students(names, '../Docs/cc.csv')
    print("第一次缺勤同学有：", ' '.join(absent))
