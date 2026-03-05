## 一、如何创建ndarray数组？
### 1.  利用列表/元组创建
- 基本语法：
```python
import numpy as np

# 一维数组
a = np.array([1, 2, 3])

# 二维数组
b = np.array([[1, 2], [3, 4]])

# 指定数据类型
c = np.array([1, 2, 3], dtype=float)
```

### 2.  使用内置函数创建特殊数组

| 函数                                   | 说明           | 示例                              |
| ------------------------------------ | ------------ | ------------------------------- |
| `np.zeros(shape)`                    | 全0数组         | `np.zeros((2,3))`               |
| `np.ones(shape)`                     | 全1数组         | `np.ones((2,3), dtype=int)`     |
| `np.empty(shape)`                    | 未初始化数组（值随机）  | `np.empty((2,2))`               |
| `np.arange(start, stop, step)`       | 类似range的等差数列 | `np.arange(1,10,2)`             |
| `np.linspace(start, stop, num)`      | 等间隔数列（含终点）   | `np.linspace(0,1,5)`            |
| `np.eye(N)`                          | 单位矩阵         | `np.eye(3)`                     |
| `np.identity(N)`                     | 单位矩阵（与eye类似） | `np.identity(3)`                |
| `np.random.random(shape)`            | [0,1)均匀分布随机数 | `np.random.random((2,2))`       |
| `np.random.randn(shape)`             | 标准正态分布随机数    | `np.random.randn(2,3)`          |
| `np.random.randint(low, high, size)` | 随机整数         | `np.random.randint(0,10,(3,3))` |

### 3. 从已有数组创建
```python
x = np.array([1,2,3])
y = np.copy(x)          # 深拷贝
z = np.asarray([4,5,6]) # 将输入转换为ndarray（如果已是ndarray则不复制）
```

---
## 二、ndarray数组有何属性？

| 属性         | 说明                     | 示例                            |
| ---------- | ---------------------- | ----------------------------- |
| `shape`    | 数组维度的元组                | `arr.shape`                   |
| `dtype`    | 元素数据类型                 | `arr.dtype`                   |
| `size`     | 元素总数                   | `arr.size`                    |
| `ndim`     | 维度数（轴数）                | `arr.ndim`                    |
| `itemsize` | 每个元素的字节大小              | `arr.itemsize`                |
| `nbytes`   | 数组总字节数（=size*itemsize） | `arr.nbytes`                  |
| `T`        | 转置视图（仅对二维有效）           | `arr.T`                       |
| `flat`     | 返回一维迭代器                | `for i in arr.flat: print(i)` |

---
## 三、ndarray数组有什么常用的方法？
### 1. 统计
| 方法                   | 说明  | 示例              |
| -------------------- | --- | --------------- |
| `sum(axis=None)`     | 求和  | `arr.sum()`     |
| `mean(axis=None)`    | 均值  | `arr.mean()`    |
| `std(axis=None)`     | 标准差 | `arr.std()`     |
| `var(axis=None)`     | 方差  | `arr.var()`     |
| `min(axis=None)`     | 最小值 | `arr.min()`     |
| `max(axis=None)`     | 最大值 | `arr.max()`     |
| `cumsum(axis=None)`  | 累积和 | `arr.cumsum()`  |
| `cumprod(axis=None)` | 累积积 | `arr.cumprod()` |

### 2. 排序

| 方法                         | 说明         | 示例           |
| -------------------------- | ---------- | ------------ |
| `sort(axis=-1, kind=None)` | 原地排序（可指定轴） | `arr.sort()` |

### 3. 数组形态修改
| 方法                  | 说明               | 示例                 |
| ------------------- | ---------------- | ------------------ |
| `reshape(newshape)` | 返回新形状的数组（不改变原数组） | `arr.reshape(3,2)` |

### 4. 其他方法
| 方法                  | 说明            | 示例                       |
| ------------------- | ------------- | ------------------------ |
| `round(decimals=0)` | 四舍五入到指定小数位数   | `arr.round(2)`           |
| `astype(dtype)`     | 转换数据类型（返回新数组） | `arr.astype(np.float32)` |


