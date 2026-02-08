## 一、如何创建ndarray数组？
### 1. array()
- 基本语法：
```python
arr = np.array([1, 2, 3])
```


### 2. arange()
- **基本语法：**
```python
arr = np.arrange(起始值, 终点值, 步长)
```

- 与`range()`类似，**==包左不包右==**

### 3. random随机生成
#### 3.1 random.randint()

#### 3.2 random.rand()

#### 3.3 random.uniform()


## 二、类型转换
- **基本语法：**
```python
arr.astype(np.float32)
```