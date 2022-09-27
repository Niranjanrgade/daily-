class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address


# Employee is derived from Person
# Person is super class of Employee
# Employee is subclass of Person
# Employee is-a Person
class Employee(Person):
    def __init__(self, id, name, address, email, salary):
        # create an object of super (Person) class object
        Person.__init__(self, name, address)

    def add_attributes(self, id, email, salary):
        self.email = email
        self.id = id
        self.salary = salary


class Student(Person):
    def __init__(self, roll, name, address, marks):
        Person.__init__(self, name, address)
        self.roll = roll
        self.marks = marks


p1 = Person('person1', 'pune')
print(f"p1 = {p1.__dict__}")

e1 = Employee(1, 'emp1', 'mumbai', 'e1@test.com', 45000)
print(f"e1 = {e1.__dict__}")

e2 =Employee(54, p1.name, p1.address, 'df', 46)
print(f"e1 = {e2.__dict__}")
