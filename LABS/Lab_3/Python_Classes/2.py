#2:
class Shape:
    def __init__(self, shapet):
        self.shapet = shapet
        self.area = 0

    def cur_area(self):

        if self.shapet == "square":
            return f"Area of Square = {self.area}"
        elif self.shapet == "rectangle":
            return f"Area of Rectangle = {self.area}"


class Square(Shape):

    def __init__(self,length):
        super().__init__("square")
        self.length = length
        self.area += self.length ** 2


print()
print("Square Area length = 5")
sharshy = Square(5)
print(sharshy.cur_area())
print()
