class Vehicle:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type


class Car:
    def __init__(self, fuel_type, model, company):
        Vehicle.__init__(self, fuel_type)
        self.model = model
        self.company = company


c = Car('d', 'm', 'c')
print(c.__dict__)
