class MyShape:
    def __init__(self, color="Red", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"MyShape: color={self.color}, is_filled={self.is_filled}"

    def getArea(self):
        return 0
    
my_shape = MyShape()
print(my_shape)
print("Area:", my_shape.getArea())