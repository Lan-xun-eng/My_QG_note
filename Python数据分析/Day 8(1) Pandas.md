# Series对象
## 一、Series的创建

### 1. 列表  
```python
s1 = pd.Series([1, 2, 3, 4, 5])  
s2 = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'], name = '数值')  
print(s1)  
print(s2)
```

### 2. 元组  
```python
s3 = pd.Series((1, 2, 3, 4, 5))  
s4 = pd.Series((1, 2, 3, 4, 5), index = ['a', 'b', 'c', 'd', 'e'], name = '数值')  
print(s3)  
print(s4)
```

### 3. 字典  
```python
s5 = pd.Series({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})  
print(s5)
```

### 4. numpy  
```python
s6 = pd.Series(np.array([1, 2, 3, 4, 5]))  
s7 = pd.Series(np.arange(5))  
s8 = pd.Series(np.arange(5), index = ['a', 'b', 'c', 'd', 'e'], name = '数值')  
print(s6)  
print(s7)  
print(s8)
```

---
## 二、Series的常用属性

- index 索引
- values 数据值

---
## 三、利用索引获取或更改元素
```python
print(s2['a'])   # 使用索引不可以直接将索引部分写出来（即s2['a']），要用print显示(即print(s2['a'])）  
s2['a'] = 7  
print(s2)
```

---
## 四、Series的排序操作


---
# DataFrame对象
## 一、如何创建DataFrame?
### 1. 字典 + 列表  
```python
data1 = {  
    'name':['张三', '李四', '王五'],  
    'gender':['女', '男', '女'],  
    'age':[11, 22, 33]  
}  
df1 = pd.DataFrame(data = data1)  
df2 = pd.DataFrame(data = data1, index=['同学'+str(i) for i in range(3)])  
print(df1)  
print(df2)  
```

### 2. 列表 + 元组  
```python
data2 = [  
    ('张三', '女', 11),  
    ('李四', '男', 22),  
    ('王五', '女', 33)  
]  
df3 = pd.DataFrame(data = data2)  
df4 = pd.DataFrame(data = data2, 
			columns=['name', 'gender', 'age'], 
			index=['同学'+str(i) for i in range(3)]
			)  
print(df3)  
print(df4)  
```
  
### 3. numpy的ndarray数组  
```python
data3 = np.arange(12).reshape(3, 4)  
df5 = pd.DataFrame(data = data3)  
df6 = pd.DataFrame(data = data3, 
				columns=['Math', 'Chinese', 'English', 'History'], 
				index=['同学'+str(i) for i in range(3)]
				)  
print(df5)  
df6
```

---
## 二、DataFrame的基本属性
- shape 维度，即行列数  
- index 行索引  
- columns 列索引，列名  
- values 数据值  
-  T 行列转置  

---
## 三、DataFrame的基本函数方法
### 1. head() 
- 查看前n行数据  
- 默认是5

### 2. tail() 
- 查看后n列  
- 同样的，默认是5

### 3. info()
- 查看df对象的详细信息  

### 4. describe() 
- 查看df对象的数学统计信息  

### 5. reset_index() 
- 重置索引列  
- drop默认是False，不删除原来索引值 -> drop = True 则删除原来索引值  

>如何理解？就是如果原本的索引就是012~这种的就没什么区别，主要是针对显式索引，所谓reset就是重置的意思，即将原本的索引变回最初的样子

---
