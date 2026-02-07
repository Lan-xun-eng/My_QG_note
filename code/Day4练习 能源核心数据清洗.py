''''
数据： raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99","120"]
处理原始数据，包括：
1. 跳过非数字项
2. 仅保留≥80的数值
3. 归一化为0.xx-1.xx小数
4. 根据结果输出状态
'''

# 1. 跳过非数字项
raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99", "120"]
nums = []
for data in raw_data:
        try:
            num = int(data)
            nums.append(num)
        except:
            print(f"跳过非数字项: {data}")
print()
print(f"跳过非数字项后的列表：{nums}")
print()

# 2. 仅保留≥80的数值
filter_nums = list(filter(lambda x: x > 0, nums))
print(f">=80的数值：{filter_nums}")
print()

# 3. 归一化
max_num = max(filter_nums)
min_num = min(filter_nums)

normalized_nums = []

for num in filter_nums:
    normalized = ((num - min_num) / (max_num - min_num)) * 2
    normalized = round(normalized, 2)
    normalized_nums.append(normalized)
print(f"归一化后的列表：{normalized_nums}")

for num in normalized_nums:
    if num > 1.0:
        print("「运转正常」 ")
    else:
        print("「核心过载」")