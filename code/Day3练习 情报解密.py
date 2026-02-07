'''
题目要求：请运用所有所学知识清洗数据：
1. 利用 String 方法去除干扰空格；
2. 利用 Set 帮特工去除重复装备；
3. 利用 Slicing 截取核心任务代号；
4. 利用 Tuple锁定坐标；
5. 最后将所有信息归档进一个 Dict档案中
'''

information = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X "
print(f"清理前的字符串：{information}")
print()

# 1. 去除空格
# 1.1 去收尾的空格
clean_information = information.strip()
# 1.2 去中间的空格
clean_parts = clean_information.split(";")
clean_list = []
for part in clean_parts:
    part = part.strip()
    clean_list.append(part)
clean_info = ";".join(clean_list)
print(f"清理后的字符串：{clean_info}")
print()

# 2. 去除重复装备
for part in clean_list:
    if part.startswith("Agent"):
        agent_info = part.split(":")[1]
    elif part.startswith("Coords"):
        coord_info = part.split(":")[1]
    elif part.startswith("Items"):
        item_info = part.split(":")[1]
    elif part.startswith("Mission"):
        mission_info = part.split(":")[1]

item_list = item_info.split(",")
unique_item = list(set(item_list))
print(f"去除重复装备后：{unique_item}")
print()

# 3. 截取核心任务代号
core_mission = mission_info[5:]
print(f"核心任务代号：{core_mission}")
print()

# 4. 锁定坐标
coord = coord_info.strip("()")
x, y = coord.split(",")
coord_touple = (int(x), int(y))
print(f"锁定的坐标：{coord_touple}")
print()

# 5. 归档
dit = {
    "Agent":agent_info,
    "Coords":coord_info,
    "Item":item_info,
    "Mission":mission_info
}
print("归档后的字典:")
for key, value in dit.items():
    print(f"{key}: {value}")
