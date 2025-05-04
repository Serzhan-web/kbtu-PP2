#1
d = {0: 'a', 1: 'b', 2: 'c'}
for x in d.values():
    print(x)

#2
a="hello"
b=list(x.upper() for x in a)
print(b)

#3
import random
print (random.choice([10.4, 56.99, 76]))

#4
d = {"john":40, "peter":45}
print(list(d.keys()))

#5
total = {}
def insert(item):
    if item in total:
        total[item] += 1
    else:
        total[item] = 1
insert('Apple')
insert('Ball')
insert('Apple')
print(len(total))

#6
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#8
class Car:
 def __init__(self, brand, model):
    self.brand = brand
    self.model = model
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")