# persons = [
#     {"name": "person1", "age": 20, "address": "pune", "email": "p1@test.com"},
#     {"name": "person2", "age": 21, "address": "mumbai", "email": "p2@test.com"},
#     {"name": "person3", "age": 22, "address": "karad", "email": "p3@test.com"},
#     {"name": "person4", "age": 23, "address": "satara", "email": "p4@test.com"},
#     {"name": "person5", "age": 24, "address": "nashik", "email": "p5@test.com"}
# ]
#
#
# def filter(person):
#     return {
#         'name': person['name'],
#         'address': person['address'],
#         'email': person['email']
#     }
#
#
# filtered_persons = list(map(filter, persons))
# print(filtered_persons)


cars = [
    {"model": "alcazar", "price": 25, "company": "hyundai"},
    {"model": "i20", "price": 11, "company": "hyundai"},
    {"model": "carens", "price": 18, "company": "kia"},
    {"model": "meridian", "price": 43, "company": "jeep"},
    {"model": "xuv700", "price": 29, "company": "mahindra"},
]


def function1():
    def filter(car):
        return {
            'model': car['model'],
            'price': car['price'],
        }

    filtered_cars = list(map(filter, cars))
    for car in filtered_cars:

        for key, value in car.items():
            print(key, end=':')
            print(value)

        print()


def function2():
    filter_affordable = lambda car: car['price'] < 20

    aff_cars = list(filter(filter_affordable, cars))
    print(aff_cars)

    def filter_names(car):
        return {
            'model': car['model']
        }

    aff_cars_names = list(map(filter_names, aff_cars))
    non_aff_cars = list(filter(lambda car: car['price'] > 20, cars))
    non_aff_car_comp = list(map(lambda car: car['company'], non_aff_cars))
    print(non_aff_car_comp)
    print(aff_cars_names)


function2()
