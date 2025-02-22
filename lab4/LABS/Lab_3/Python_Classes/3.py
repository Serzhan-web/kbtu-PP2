#3

class Rectangle(Shape):

    def __init__(self,length, width):
        super().__init__("rectangle")
        self.length = length
        self.width = width
        self.area += self.length * self.width


tiktt = Rectangle(6,10)

print("Area of Rectangle l = 6, w = 10")
print(tiktt.cur_area())
print()
