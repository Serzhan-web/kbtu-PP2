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


color_input = input("Enter color for Rectangle (default is Blue): ").strip() or "Blue"
x_input = float(input("Enter x coordinate of the top-left corner (default is 0): ").strip() or 0)
y_input = float(input("Enter y coordinate of the top-left corner (default is 0): ").strip() or 0)
length_input = float(input("Enter the length of the rectangle (default is 1): ").strip() or 1)
width_input = float(input("Enter the width of the rectangle (default is 1): ").strip() or 1)

user_rectangle = Rectangle(color=color_input, x_top_left=x_input, y_top_left=y_input, length=length_input, width=width_input)

print(user_rectangle)
print("Area:", user_rectangle.getArea())
