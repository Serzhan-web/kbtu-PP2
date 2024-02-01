import math

class Point():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        self.x = float(input("x:"))
        self.y = float(input("y:"))
        self.z = float(input("z:"))

    def dist(self):
        x1 = float(input("x1:"))
        y1 = float(input("y1:"))
        z1 = float(input("z1:"))
        return math.sqrt((x1 - self.x)**2 + (y1 - self.y)**2 + (z1 - self.z)**2)

initial_x = float(input("Initial x:"))
initial_y = float(input("Initial y:"))
initial_z = float(input("Initial z:"))

point = Point(initial_x, initial_y, initial_z)
point.show()
distance = point.dist()
print("Distance between points:", distance)
