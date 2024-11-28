# 方法1：使用新列表
def remove_duplicates_new_list(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:  # 保持元素顺序
            unique_list.append(item)
    return unique_list

# 方法2：使用集合
def remove_duplicates_set(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:  # 保持顺序
            seen.add(item)
            unique_list.append(item)
    return unique_list

# 测试列表
original_list = [1, 1, 2, 2, 3, 3, 'a', 'a']

# 方法1去重
result1 = remove_duplicates_new_list(original_list)
print("After removing duplicates (method 1):", result1)

# 方法2去重
result2 = remove_duplicates_set(original_list)
print("After removing duplicates (method 2):", result2)
