class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.employees = []
        self.counter = 0

    def add(self, name, address):
        name, address = name, address
        tup =
        self.employees.extend(tup)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.employees):
            raise StopIteration
        employee = self.employees[self.counter]
        employee = self.employees[self.counter]

        self.counter += 1
        return employee


company = Company('n', 'a')

company.add('a', 'p')
company.add('b', 'p')
company.add('c', 'p')
company.add('d', 'p')

for employee in company:
    print(employee)
