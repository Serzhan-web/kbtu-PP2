class MyShape:
    def __init__(self, color="Red", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"MyShape: color={self.color}, is_filled={self.is_filled}"

    def getArea(self):
        return 0


class Rectangle(MyShape):
    def __init__(self, color="Blue", is_filled=True, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle: color={self.color}, is_filled={self.is_filled}, x_top_left={self.x_top_left}, " \
               f"y_top_left={self.y_top_left}, length={self.length}, width={self.width}"


class Circle(MyShape):
    def __init__(self, color="Green", is_filled=True, x_center=0, y_center=0, radius=1):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        import math
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle: color={self.color}, is_filled={self.is_filled}, x_center={self.x_center}, " \
               f"y_center={self.y_center}, radius={self.radius}"

length=int(input("length:"))
width=int(input("width:"))

rectangle = Rectangle(length, width)
print(rectangle)
print("Area:", rectangle.getArea()) 

radius=int(input())
circle = Circle(radius)
print(circle)
print("Area:", circle.getArea())  
