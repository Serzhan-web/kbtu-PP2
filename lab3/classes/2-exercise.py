class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

# Example usage:
# Create instances of Shape and Square
shape_instance = Shape()
square_instance = Square(5)

# Call the area function for both instances
print("Area of Shape:", shape_instance.area())  # Output: 0
print("Area of Square:", square_instance.area())  # Output: 25
