import csv
import os


# 读取学生名单
def read_student_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


# 检查全勤同学
def find_full_attendance(names, attendance_files):
    attendance_count = {name: 0 for name in names}

    for attendance_file in attendance_files:
        with open(attendance_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            present_students = {row[0] for row in reader}
            for name in present_students:
                if name in attendance_count:
                    attendance_count[name] += 1

    full_attendance_students = [name for name, count in attendance_count.items() if count == len(attendance_files)]
    return full_attendance_students


# 主程序
if __name__ == "__main__":
    names = read_student_names('../Docs/Name.txt')
    attendance_files = [f"{i}.csv" for i in range(1, 11)]
    full_attendance = find_full_attendance(names, attendance_files)
    print("全勤同学有：", ' '.join(full_attendance))
