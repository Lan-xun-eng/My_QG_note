# 类
## 一、什么是类与对象？
- **类（Class）**：描述一组数据和行为的“蓝图”，用来创建对象
- **对象（Object）**：类的实例，也就是具体的实体

- **举个栗子**
```python
class Animal:
    pass

dog = Animal()  # dog是Animal类的一个对象
```

---
## 二、如何定义类？

- **基本语法：**
```python
class 类名:
    # 属性（成员变量）
    # 方法（成员函数）
```

- **举个栗子**
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 属性
        self.age = age

    def greet(self):
        print(f"你好，我是{self.name}，今年{self.age}岁")
```

---
## 三、如何创建对象？

```python
p1 = Person("小明", 18)
p1.greet()  # 输出：你好，我是小明，今年18岁
```

---
## 四、成员变量和方法

- **成员变量（属性）：** 对象的数据，或者说对象的状态特性
- **成员方法（方法）：** 定义对象可以做什么，即对象的行为

```python
class Dog:
    def __init__(self, name):
        self.name = name              # 成员变量

    def bark(self):                   # 成员方法
        print(f"{self.name}：汪汪！")
```
使用：
```python
d = Dog("旺财")
d.name     # 调用属性
d.bark()   # 调用方法 -> 输出：旺财：汪汪！
```

---
## 五、self 关键字

- `self`  代表  **对象自身**
- 在成员方法的第一个参数中==必须写（定义时）==，**==调用时不传==**
- 用来访问对象自己的属性和方法

- **举个栗子**
```python
class Student:
    def set_name(self, name):
        self.name = name
```

---
## 六、构造方法（初始化）

- 名为 `__init__`
- 对象创建时**自动运行**
- 用来初始化成员变量

```python
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
```

---
## 七、特殊方法（魔术方法）

- 以==**双下划线**==开始和结束的函数（如`__str__`、`__eq__`）
- 用于定制对象的行为

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"《{self.title}》"

b = Book("Python基础")
print(b)  # 输出： 《Python基础》
```

---
## 八、封装（私有成员）

- 私有变量和方法：前面加两个下划线，如 `__age`
- 只能在类内部访问，外部不可访问
- 和成员变量一起定义，一起初始化，只是使用的时候不同而已

- **举个栗子**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有变量

    def get_balance(self):
        return self.__balance
```

- 注意区分私有成员和特殊方法，前者是前面加两个下划线，后者是前后加两个下划线

---
## 九、继承

### 1. 什么是继承？
- 让子类自动拥有父类的属性和方法

### 2. 单继承
```python
class Parent:
    def say(self):
        print("hello")

class Child(Parent):
    pass

c = Child()
c.say()  # 输出：hello
```

### 3. 多继承
```python
class A:
    def feature_a(self):
        print("A特性")

class B:
    def feature_b(self):
        print("B特性")

class C(A, B):
    pass

c = C()
c.feature_a()  # 输出：A特性
c.feature_b()  # 输出：B特性
```

---
## 十、复写（方法重写）

- 子类可以重新定义父类的方法，主要用于实现不同功能
- 即子类继承父类的方法后，对父类的方法不甚满意，那么可以对父类的方法进行复写
- 复写后该方法在子类中改变了，但是

```python
class Animal:
    def speak(self):
        print("普通动物叫声")

class Cat(Animal):
    def speak(self):
        print("喵喵！")

c = Cat()
c.speak()  # 输出：喵喵！
```

---

## 十一、多态

- 不同类的对象可以用同一个方法名，各自表现不同
```python
def animal_speak(animal):
    animal.speak()

cat = Cat()
dog = Dog("旺财")
animal_speak(cat)
animal_speak(dog)
```

---

## 十二、类方法和静态方法

- **类方法**：用 `@classmethod` 装饰，参数是 `cls`，表示类本身。
- **静态方法**：用 `@staticmethod` 装饰，没有 `self` 或 `cls`。

**举个栗子**
```python
class Demo:
    count = 0

    @classmethod
    def show_count(cls):
        print(f"共有{cls.count}个对象")

    @staticmethod
    def welcome():
        print("欢迎学习Python类")
```

---
