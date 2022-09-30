class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(self.name)
        print(self.age)


class Employee(Person):
    def __init__(self, name, age, email, salary, id):
        Person.__init__(self, name, age)
        self.email = email
        self.salary = salary
        self.id = id

    def print_details(self):
        Person.print_details(self)
        print(self.email)
        print(self.salary)
        print(self.id)


class Player(Person):
    def __init__(self, name, age, team):
        Person.__init__(self, name, age)
        self.team = team

    def print_details(self):
        Person.print_details(self)
        print(self.team)


e = Employee('n', 10, 'e', 55, 4)
e.print_details()

p = Player('n', 5, 't')
p.print_details()


