class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, id, subject):
        super().__init__(self, name, age)
        self.id = id
        self.subject = subject

x = Student("Anna", 19, 1, ["history", "biology"])
x = Person("Grey", 18)