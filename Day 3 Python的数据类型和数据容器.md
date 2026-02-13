# 简单数据类型
## 一、整数int

---
## 二、浮点数float

---
## 三、字符串
### 1. 基本语法
- **单引号/双引号/三引号** 皆可
```python
# 单引号
s1 = 'Hello'
# 双引号
s2 = "World"
# 三引号（可跨行，保留格式）
s3 = '''这是一个
多行
字符串'''
```

### 2. 字符串是不可变的
- 字符串一旦创建，内部字符不能修改
- 所有看似“修改”的操作，其实都是创建了新的字符串对象

### 3. 字符串的加减法：
- `+` ：**连接**多个字符串，拼接成长字符串
- `*` ：**复制**字符串，扩张多少倍

### 4. 常用字符串方法
#### （1） 大小写转换
- `upper()`   **全部改为大写**
- `lower()`   **全部改为小写**
- `capitalize()`   **首字母大写，其余小写**
- `title()`   **每个单词首字母大写**
- `swapcase()`   **大小写互换**
```python
s = 'hello World'

s.upper()          # 'HELLO WORLD'
s.lower()          # 'hello world'
s.capitalize()     # 'Hello world'（首字母大写，其余小写）
s.title()          # 'Hello World'（每个单词首字母大写）
s.swapcase()       # 'HELLO wORLD'（大小写互换）
```

#### （2）查找统计
- `find() `       **第一次出现的位置，找不到返回-1**
- `rfind()`       **从右找第一次出现的位置**
- `count()  `     **统计子串出现次数**
```python
s = 'hello world'

s.find('o')        # 4（第一次出现的位置，找不到返回-1）
s.rfind('o')       # 7（从右找第一次出现的位置）
s.count('l')       # 3（统计子串出现次数）
'world' in s       # True（成员判断）
```

#### （3）去除空白
- **作用：** 清楚字符串首尾的空格
- `lstrip()` 和 `rstrip()` 分别指 清除左边/右边的空格
- `strip()` 还可以指定去除的内容

```python
s = '  hello  \n'

s.strip()          # 'hello'（去除两端空白字符）
s.lstrip()         # 'hello  \n'（去除左侧空白）
s.rstrip()         # '  hello'（去除右侧空白）

# 可指定要去除的字符
s2 = '---abc---'
s2.strip('-')      # 'abc'
```

#### （4）分割连接
- `split()`   **将字符串按指定分隔符拆分为列表**
- `partition() `   **只分割一次，返回三部分（分隔符前、分隔符本身、分隔符后）**
- `join()`   **将可迭代对象中的字符串连接成一个字符串**
- `splitlines()`   **按行拆分**
>所谓按行就是看 `\n` 

```python
# split() 将字符串按指定分隔符拆分为列表
s = 'apple,banana,orange'
s.split(',')       # ['apple', 'banana', 'orange']

# partition() 只分割一次，返回三部分（分隔符前、分隔符本身、分隔符后）
s.partition(',')   # ('apple', ',', 'banana,orange')

# join() 将可迭代对象中的字符串连接成一个字符串
sep = '-'
sep.join(['2025', '03', '28'])   # '2025-03-28'

# splitlines() 按行拆分
lines = '第一行\n第二行'
lines.splitlines()  # ['第一行', '第二行']
```

#### （5）替换
- `replace()`   替换

```python
s = 'hello world'

s.replace('world', 'Python')  # 'hello Python'

# 可指定替换次数
s = 'a-b-c-d'
s.replace('-', '+', 2)        # 'a+b+c-d'（只替换前2个）
```

#### （6）startswith( )
- **基本语法：**
```python
str.startswith(prefix[, start[, end]])
```
- `prefix`：要检查的前缀，可以是字符串或字符串元组
- `start`：开始检查的位置（默认从开头开始）
- `end`：结束检查的位置（默认到字符串末尾）

### 5. 索引与切片
- **从0开始** 
- `[正数]` 从左到右
  `[负数]` 从右到左
```python
s = 'Python'

# 索引（从0开始）
s[0]   # 'P'
s[-1]  # 'n'（负数从右往左，-1为最后一个）

# 切片 [start:stop:step]
s[0:3]    # 'Pyt'（包含start，不包含stop）
s[:3]     # 'Pyt'（省略start表示从开头）
s[3:]     # 'hon'（省略stop表示到结尾）
s[::2]    # 'Pto'（步长2）
s[::-1]   # 'nohtyP'（反向字符串）
```

### 6. 字符串格式化

- **f-string**
```python
name = 'Alice'
age = 25
print(f'姓名：{name}，年龄：{age}')  # 姓名：Alice，年龄：25

# 可执行表达式
print(f'10年后年龄：{age + 10}')     # 10年后年龄：35

# 调用方法
print(f'大写：{name.upper()}')      # 大写：ALICE
```

- **str.format() 方法**
```python
'姓名：{}，年龄：{}'.format('Bob', 30)        # 姓名：Bob，年龄：30
'姓名：{name}，年龄：{age}'.format(name='Tom', age=22)
```

- **格式化（类似C语言printf）** 
```python
'姓名：%s，年龄：%d' % ('Jack', 28)   # 姓名：Jack，年龄：28
```

---
## 四、布尔类型

- 布尔类型只有2种值：**Ture/Flase**
- Ture/Flase的首字母一定要**大写**

### 1. 逻辑运算
- **and or not : 与 或 非**
- 优先级：not > and > or  

---
## 五、空值NoneType

---
# 数据容器
## 一、列表
### 1.1 如何创建列表？
- 列表可以加入**任何东西**，其中的元素之间可以**没有任何关联**

```python
# 空列表
lst1 = []
lst2 = list()

# 带初始值
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4]
mixed = [1, 'hello', 3.14, True]   # 可存放不同类型

# 使用list()转换其他可迭代对象
list('abc')      # ['a', 'b', 'c']
list(range(5))   # [0, 1, 2, 3, 4]
```

### 1.2 索引和切片
- 索引和切片都是 ==从 0 开始的==

```python
lst = ['a', 'b', 'c', 'd', 'e']

# 索引
lst[0]     # 'a'
lst[-1]    # 'e'

# 切片
lst[1:4]   # ['b', 'c', 'd']
lst[:3]    # ['a', 'b', 'c']
lst[::2]   # ['a', 'c', 'e']
lst[::-1]  # ['e', 'd', 'c', 'b', 'a']

# 切片赋值（修改部分元素）
lst[1:3] = ['x', 'y']   # lst变为 ['a', 'x', 'y', 'd', 'e']
```

### 1.3 列表常用方法
#### 添加元素
- `append( 元素 )`   ：   从列表末尾添加元素
- `insert[ 索引 , 元素 ]`  ：   在列表中插入元素，在任何位置添加新元素

```python
lst = ['a', 'b']

# append(): 在末尾添加单个元素
lst.append('c')          # ['a', 'b', 'c']

# insert(): 在指定索引位置插入元素
lst.insert(1, 'x')       # ['a', 'x', 'b', 'c', 'd', 'e']

# extend(): 将可迭代对象的元素逐个添加到末尾
lst.extend(['d', 'e'])   # ['a', 'b', 'c', 'd', 'e']
```

#### 删除元素
- `del( 索引 )`
  删除列表中任意位置的元素
- `pop( )`
   删除列表末尾的元素+接着使用它 → 在pop( 索引 )加入索引，则可以删除并弹出列表中的任意元素
- `remove( 元素 )`
  删除列表中某一元素的值
	- remove( )只删除第一个指定的值，所以如果列表中有多个这样的值并要全部删除，则需要使用循环

```python
lst = ['a', 'b', 'c', 'b', 'd']

# remove(): 删除第一个匹配的元素，不存在则报错
lst.remove('b')          # ['a', 'c', 'b', 'd']

# pop(): 删除并返回指定索引位置的元素（默认最后一个）
lst.pop()                # 返回 'd'，列表变为 ['a', 'c', 'b']
lst.pop(1)               # 返回 'c'，列表变为 ['a', 'b']

# clear(): 清空列表
lst.clear()              # []

# del语句
lst = ['a', 'b', 'c']
del lst[1]               # ['a', 'c']
del lst[0:2]             # 切片删除
del lst                  # 删除整个变量
```

#### 排序反转
```python
numbers = [3, 1, 4, 1, 5]

# sort(): 原地排序（直接修改列表）
numbers.sort()           # [1, 1, 3, 4, 5]
numbers.sort(reverse=True)  # [5, 4, 3, 1, 1]

# sorted(): 返回新列表，原列表不变
sorted(numbers)          # 新列表 [1, 1, 3, 4, 5]

# reverse(): 原地反转列表顺序
numbers.reverse()        # 反转，依赖于当前顺序

# 切片反转（生成新列表）
new_lst = numbers[::-1]
```

#### 复制列表
- 直接赋值是引用，不是复制

```python
# 直接赋值是引用，不是复制
lst1 = [1, 2, 3]
lst2 = lst1           # lst2与lst1指向同一对象

# 浅拷贝（只拷贝第一层）
lst3 = lst1.copy()    # 方法1
lst4 = lst1[:]        # 方法2
lst5 = list(lst1)     # 方法3
```

### 1.4 列表元素删除的方法如何选择？
- 知道元素的==位置== → 用del()
- 知道要删除元素的==值== → 用remove()
- 知道位置，但想在删除元素后还能==继续使用==它 → 用pop()


---

## 二、元组
### 2.1 如何创建元组？
```python
# 空元组
t1 = ()
t2 = tuple()

# 单个元素的元组（必须加逗号）
t3 = (1,)          # 注意逗号，不加逗号是整数1
t4 = 1,            # 可以省略括号，但逗号不能少

# 多个元素的元组
t5 = (1, 2, 3)
t6 = 4, 5, 6       # 括号可省略

# tuple()转换
tuple('abc')       # ('a', 'b', 'c')
```

---

## 三、集合：
### 3.1 如何创建集合？
```python
# 空集合（必须用set()，因为{}是空字典）
s1 = set()

# 正常创建
s2 = {1, 2, 3, 4}
s3 = set([1, 2, 2, 3])   # 自动去重，结果为 {1, 2, 3}
s4 = set('hello')        # {'h', 'e', 'l', 'o'}（无序，注意l只有一个）
```

- 与字典的主要区别在于：字典的{}中是**键值对**，而集合的{}中是**元素即值**
- 集合中每个元素都是独一无二的，即集合中的元素**不能重复**

---
# 四、字典
### 4.1 如何创建字典？
- 字典中的键和值可以是**任何类型**  

```python
# 空字典
d1 = {}
d2 = dict()

# 正常创建
student = {'name': '张三', 'age': 20, 'score': 95.5}

# 使用dict()构造函数
d3 = dict(name = '李四', age = 22)      # 注意键名不加引号，但必须是合法标识符
d4 = dict([('a',1), ('b',2)])      # 从键值对序列创建

# 使用fromkeys()创建默认值字典
keys = ['x', 'y', 'z']
d5 = dict.fromkeys(keys, 0)        # {'x':0, 'y':0, 'z':0}
```

### 4.2 增删改查
#### 增
- `字典名[ 新的键 ] = 新的值`
- 新添加的键值对直接接在字典的末尾

#### 删
- `del 字典名[ 要删除的键 ]`
- `pop( )`

#### 该
- `字典名[ 键 ] = 新的值`

#### 查
- **字典名[ 键 ]**  
- **get( 键 ，指定的键不存在时要返回的值 )**  
- 选择： 如果指定的键如果有可能不存在则使用get() 一般都用字典名[ 键 ]  

### 4.3 清空字典：
- `clear()`

### 4.4 遍历字典：
- 遍历字典时，一定要先将**字典**转换成**列表** → ==**字典名.items()**==

```python
user_0 = {	'username':'efermi',	'first':'enrico',	'last':'fermi'}

for key,value in user_0.items():	
	print(key)
	print(value)
```

### 4.5 字典的常用方法：
- **字典名.keys()** → 遍历字典中的所有键  
- **sorted(字典名.keys())** → 按特定顺序遍历字典中的所有值  
- **字典名.values()** → 遍历字典中的所有值  
- 同样的，注意是**keys() ， values()**  
- **set( 字典名.values() )** → 去除字典中值的重复项 → 本质上就是集合

### 4.6 字典推导式
- `{键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}`

```python
# 生成数字平方字典
squares = {x: x**2 for x in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}

# 过滤并转换
items = ['apple', 'banana', 'orange']
d = {item: len(item) for item in items if len(item) > 5}  
# {'banana':6, 'orange':6}
```

---
# 嵌套

### 列表中储存字典：

```python
alien1 = {'color':'green','point':'5'}alien2 = {'color':'yellow','point':'10'}alien3 = {'color':'red','point':'15'}aliens = ['alien1','alien2','alien3']for alien in aliens:	print(alien)
```

### 字典中储存列表：

```python
pizza = {	'crust':'thick'	'toppings':['mushrooms','extra cheese'],	}
```

### 字典中储存字典：

- 每一个嵌套的字典都应有相同的结构 → 会使得嵌套的字典更容易处理

```python
users = {	'a': {		'first':'albert',		'last':'einstein',		'location':'princeton',		},	'b': {		'first':'marie',		'last':'curie',		'location':'paris',		},	}
```

# 列表与字典的爱恨情仇

- 需要表示数据间的内在联系+只需要一排数据时，则用列表
- 不仅需要表示数据间的内在联系+只需要一排数据，还需要能找到数据，则用字典