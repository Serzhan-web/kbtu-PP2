#4

print("Another Two points problem...")
print()

class Point:


    def __init__(self, x,y):
        self.x = x
        self.y = y

    def show(self):
        return f"coordinates: x = {self.x}, y = {self.y}"

    def move(self):
        print("Choose how to change the coords:")
        print("x,y ->", end=": ")

        self.x, self.y = [int(i) for i in input().split(',')]

        print()
        print(f"Coords was successfully changed to {self.x}, {self.y}")
        print()

    def dist(self, point):

        q = (point.x - self.x) ** 2
        w = (point.y - self.y) ** 2

        e = (q + w) ** 0.5
        return f"Dist between two points equals to: {e}"


a = Point(0,0)
b = Point(1,1)

print()
print(a.show())
print(b.show())
print()

a.move()

print()
print(a.show())
print(b.show())
print()

print(a.dist(b))
print()
