import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(r'E:\\pycharm项目\\QG')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 导入数据
df = pd.read_csv(".\\train.csv")

# 查看数据集的相关信息
print(df.info())
print("\n")
print(df.describe())
print("\n")

# 可视化泰坦尼克号乘客生还几率
# 3.1 总体生还率
x = df['Survived'].value_counts()
plt.figure(figsize = (10,10), dpi = 100)
plt.pie(x, labels=['死亡','存活'], autopct = '%.2f%%', explode = (0,0.1), shadow = True)
plt.title('泰坦尼克号乘客生还几率饼图', fontsize = 20)
plt.legend(loc = 'best', fontsize = 12)
plt.savefig(".\Titanic survival probability pie chart")
plt.show()

# 3.2 不同性别乘客生还几率
## 准备数据
sex_count = df.groupby(by = 'Sex')['Survived'].value_counts()
female_data = sex_count.loc['female'][::-1]
male_data = sex_count.loc['male'][::-1]
# print(sex_count)
## 创建画布
fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (12, 8), dpi = 100)
## 绘制图像
axes[0].pie(female_data,
            labels=['死亡率','存活率'],
            autopct = '%.2f%%',
            colors = ['#9400D3', '#FFB6C1'],
            explode = (0,0.1),
            shadow = True
            )
axes[1].pie(male_data,
            labels=['死亡率','存活率'],
            autopct = '%.2f%%',
            colors = ['#2E8B57', '#AFEEEE'],
            explode = (0,0.1),
            shadow = True
            )
axes[0].set_title('泰坦尼克号女性乘客生还几率饼图', fontsize = 20)
axes[1].set_title('泰坦尼克号男性乘客生还几率饼图', fontsize = 20)
axes[0].legend(loc = 'best', fontsize = 12)
axes[1].legend(loc = 'best', fontsize = 12)
plt.savefig(".\Survival Rate by Gender Pie Chart")
## 显示图像
plt.show()


# 3.3 不同年龄段乘客生还几率
## 准备数据
print(f"泰坦尼克号的乘客中\n"
      f"年龄最小的是{df['Age'].min()}岁\n"
      f"最大的是{df['Age'].max()}岁"
      )
x = list(range(0, 81, 5))
x_positions = [x[i] + (x[i+1] - x[i])/2 for i in range(len(x)-1)]

age_total, _ = np.histogram(df['Age'], range = [0,80], bins = 16)  # 总人数分组

age_survived = []   # 生还人数分组
for age in range(5, 81, 5):
    survived_num = df.query('Age >= @age-5 and Age < @age')['Survived'].sum()
    age_survived.append(survived_num)
## 创建画布
plt.figure(figsize = (12, 8), dpi = 100)
## 绘制图像
plt.bar(x_positions,
        age_total,
        width = 5,
        edgecolor = 'black',
        color = '#2E8B57',
        label = '总人数',
        alpha = 0.8
        )
plt.bar(x_positions,
        age_survived,
        width = 5,
        edgecolor = 'black',
        color = '#AFEEEE',
        label = '生还人数',
        alpha = 0.8
        )
plt.grid(linestyle = '--', alpha = 0.3)
plt.title('不同年龄段乘客生还人数柱状图', fontsize = 20)
plt.xlabel('年龄区间（岁）', fontsize=12)
plt.ylabel('人数（人）', fontsize=12)
plt.legend(loc = 'best', fontsize = 12)
plt.tight_layout()
plt.savefig(".\\Number of Passengers and Survivors by Age Group Bar Chart")
## 显示图像
plt.show()


# 3.4 不同登入港口乘客的生还几率
print(f"登入港口分别有：\n"
      f"{df['Embarked'].drop_duplicates().dropna().reset_index(drop = True)}")
## 准备数据
embarked_count = df.groupby(by = 'Embarked')['Survived'].value_counts()
C_count = embarked_count.loc['C'][::-1]
Q_count = embarked_count.loc['Q'][::-1]
S_count = embarked_count.loc['S'][::-1]
## 创建画布
fig1, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (14, 8), dpi = 100)
## 绘制图像
axes[0].pie(C_count,
            labels=['死亡率','存活率'],
            autopct = '%.2f%%',
            colors = ['#2E8B57', '#AFEEEE'],
            explode = (0, 0.1),
            shadow = True,
            )
axes[0].set_title('泰坦尼克号C登入口乘客生还几率饼图', fontsize = 15)
axes[0].legend(loc = 'upper left', fontsize = 10)

axes[1].pie(Q_count,
            labels = ['死亡率','存活率'],
            autopct = '%.2f%%',
            colors = ['#9400D3', '#FFB6C1'],
            explode = (0, 0.1),
            shadow = True,
            )
axes[1].set_title('泰坦尼克号Q登入口乘客生还几率饼图', fontsize = 15)
axes[1].legend(loc = 'best', fontsize = 10)

axes[2].pie(Q_count,
            labels = ['死亡率','存活率'],
            autopct = '%.2f%%',
          # colors = ['#9400D3', '#FFB6C1'],
            explode = (0, 0.1),
            shadow = True,
            )
axes[2].set_title('泰坦尼克号S登入口乘客生还几率饼图', fontsize =15)
axes[2].legend(loc = 'best', fontsize = 10)
plt.tight_layout()
plt.savefig(".\Survival Rate by Embarked Pie Chart")
## 展示图像
plt.show()


# 3.5 不同船舱等级乘客生还几率
print(f"船舱等级有：")
print([f"{i}级" for i in df['Pclass'].drop_duplicates().sort_values().values])
## 准备数据
pclass_count = df.groupby(by = 'Pclass')['Survived'].value_counts()

first_count = pclass_count.loc[1][::-1]
second_count = pclass_count.loc[2][::-1]
third_count = pclass_count.loc[3][::-1]
## 创建画布
fig2, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (15, 8), dpi = 100)
## 绘制图像
axes[0].pie(first_count,
            labels = ['死亡率', '生存率'],
            autopct = '%.2f%%',
            colors = ['#FF6B8B', '#3A86FF'],
            explode = (0, 0.1),
            shadow = True
            )
axes[0].set_title('泰坦尼克号一级船舱乘客生还几率饼图', fontsize = 15)
axes[0].legend(loc = 'best', fontsize = 10)

axes[1].pie(second_count,
            labels = ['死亡率', '生存率'],
            autopct = '%.2f%%',
            colors = ['#06D6A0', '#EF476F'],
            explode = (0, 0.1),
            shadow = True
            )
axes[1].set_title('泰坦尼克号二级船舱乘客生还几率饼图', fontsize = 15)
axes[1].legend(loc = 'best', fontsize = 10)

axes[2].pie(third_count,
            labels = ['死亡率', '生存率'],
            autopct = '%.2f%%',
            colors = ['#6C63FF', '#FFD166'],
            explode = (0, 0.1),
            shadow = True
            )
axes[2].set_title('泰坦尼克号三级船舱乘客生还几率饼图', fontsize = 15)
axes[2].legend(loc = 'best', fontsize = 10)
plt.tight_layout()
plt.savefig(".\Survival Rate by Pclass Pie Chart")
plt.show()


# 3.6 不同票价乘客的生还率
## 准备数据
fare_count = df.groupby(by = 'Fare')['Survived'].value_counts()
fare_count = pd.DataFrame(fare_count)
fare_count.reset_index(inplace = True)

fare_tatal = fare_count.groupby(by = 'Fare')['count'].sum()
fare_tatal = pd.DataFrame(fare_tatal)
fare_tatal.reset_index(inplace = True)
fare_tatal.rename(columns = {'count':'Tatal_count'}, inplace = True)

fare_survived = fare_count.query('Survived == 1')
fare_survived.reset_index(drop = True, inplace = True)
fare_survived.rename(columns = {'count':'Survived_count'}, inplace = True)

fare_death = fare_count.query('Survived == 0')
fare_death.rename(columns = {'count':'Death_count'}, inplace = True)

fare_survived_rate = pd.merge(fare_survived, fare_tatal, on = 'Fare', how = 'inner')
fare_death_rate = pd.merge(fare_death, fare_tatal, on = 'Fare', how = 'inner')

survived_rate = fare_survived_rate['Survived_count']/fare_survived_rate['Tatal_count']
survived_rate.index = fare_survived['Fare']

death_rate = fare_death_rate['Death_count']/fare_death_rate['Tatal_count']
death_rate.index = fare_death['Fare']
## 创建画布
fig3, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (16, 6), dpi = 100)
## 绘制图像
axes[0].scatter(survived_rate.index,
                survived_rate,
                s = 50,
                marker = 'o',
                color = '#9400D3'
                )
axes[0].set_title('乘客生还率和票价关系散点图', fontsize = 20)
axes[0].grid(linestyle = '--', alpha = 0.3)
axes[1].scatter(death_rate.index,
                death_rate,
                s = 50,
                marker = '^',
                color = '#FFB6C1'
                )
axes[1].set_title('乘客死亡率和票价关系散点图', fontsize = 20)
axes[1].grid(linestyle = '--', alpha = 0.3)
plt.tight_layout()
## 显示图像
plt.show()
