import math

class Shape:
    total_shapes = 0

    def __init__(self):
        self.__area = None
        Shape.total_shapes += 1

    def _calc_area(self):
        raise NotImplementedError

    def get_area(self):
        if self.__area is None:
            self.__area = self._calc_area()
            print(f"由计算得，面积是： {self.__area}")
        return self.__area

    @classmethod
    def get_total_shapes(cls):
        return cls.total_shapes


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        print(f"创建了一个圆形，半径是 {radius}")

    def _calc_area(self):
        # 圆形面积 = π × 半径²
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        print(f"创建了一个矩形，宽 {width}，高 {height}")

    def _calc_area(self):
        # 矩形面积 = 宽 × 高
        return self.width * self.height


# 1. 创建图形
circle1 = Circle(5)  # 圆形1，半径5
circle2 = Circle(3)  # 圆形2，半径3
rectangle1 = Rectangle(4, 6)  # 矩形1，宽4高6
rectangle2 = Rectangle(2, 8)  # 矩形2，宽2高8

# 2. 获取面积（多态体现：用同样的方法获取不同图形的面积）
shapes = [circle1, circle2, rectangle1, rectangle2]

print()
for i in range(len(shapes)):
    area = shapes[i].get_area()
    print(f"则图形{i+1}的面积是: {area:.2f}")
print()

# 3. 获取创建图形的数量
print(f"目前一共创建了{Shape.get_total_shapes()}个图形")
print()

# 4. 验证是否确实不能直接访问私有属性
try:
    print(f"尝试直接看圆形的面积: {circle1.__area}")
except AttributeError as e:
    print(f"错误信息: {e}")
    print("说明：不能通过__area直接获取图形面积，必须通过get_area()获得")
