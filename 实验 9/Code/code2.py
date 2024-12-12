from collections import Counter

list1 = ["理工", "理工", "理工", "师范", "综合", "农林", "理工", "综合", "理工", "理工",
         "综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", "综合", "综合",
         "师范", "理工", "综合", "理工", "综合", "综合", "综合", "综合", "综合", "理工",
         "理工", "综合", "理工", "综合", "综合", "理工", "农林", "民族", "军事"]

counter = Counter(list1)
for school_type, count in counter.items():
    print(f"{school_type}: {count}")
