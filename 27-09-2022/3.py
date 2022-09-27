class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_e_details(self):
        print(self.id)
        print(self.name)


class Manager(Employee):
    def __init__(self, id, name, department):
        Employee.__init__(self, id, name)
        self.department = department

    def print_m_details(self):
        print(self.id)
        print(self.name)
        print(self.department)


e = Employee(87, 'r')
e.print_e_details()

e = Manager(e.id, e.name, 'j')
e.print_m_details()

m = Manager(45, 'n', 'd')
print(m.__dict__)
m.print_e_details()
m.print_m_details()
