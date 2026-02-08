import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(r'E:\\pycharm项目\\QG')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

file_path = "E:\\pycharm项目\\QG\\加州房价.txt"
house_df = pd.read_csv(file_path)

# 1. 查看房价的相关信息
print(house_df.head())
print("\n")
print(house_df.tail())
print("\n")
house_df.info()
print("\n")
print(house_df.describe())
print("\n")

# 可视化
# 1. 准备数据
y = house_df['median_house_value']
x = range(len(y))

# 2. 创建画布
plt.figure(figsize = (14, 8), dpi = 120)

# 3.1 绘制初始折线图
plt.hist(y, bins=50, edgecolor='black',color = 'steelblue', alpha=0.7)

# 3.2 添加网格
plt.grid(linestyle = '--', alpha = 0.3)

# 3.3 添加标题
plt.title("加州房价分布直方图", fontsize = 20)

# 3.4 添加标签
plt.xlabel("房价(美元)", fontsize = 12)
plt.ylabel("频数", fontsize = 12)

# 3.5 优化布局
plt.tight_layout()

# 3.6 保存图片
plt.savefig('.\house_values_histogram.png', dpi = 100)

# 4. 显示图像
plt.show()
