class Person:
    def __init__(self):
        self.name = 'a'
        self.age = 10


class Player(Person):
    def __init__(self):
        Person.__init__()


class Employee(Person):
    def __init__(self):
        pass


class Student(Person):
    pass


p = Player()
e = Employee()
s = Student()