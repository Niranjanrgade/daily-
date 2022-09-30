def function3():
    cars = [
        {"model": "alcazar", "price": 25, "company": "hyundai"},
        {"model": "i20", "price": 11, "company": "hyundai"},
        {"model": "carens", "price": 18, "company": "kia"},
        {"model": "meridian", "price": 43, "company": "jeep"},
        {"model": "xuv700", "price": 29, "company": "mahindra"},
    ]

    # price <= 20 => affordable else not affordable
    # ['NOT AFFORDABLE', 'AFFORDABLE', ...]

    li = ['Not affordable' if car['price'] > 20 else 'Affordable' for car in cars]
    print(li)

    li2 = list(map(lambda car: 'Not affordable' if car['price'] > 20 else 'Affordable', cars))
    print(li2)

    tup = tuple('Not affordable' if car['price'] > 20 else 'Affordable' for car in cars)
    print(tup)


# function3()


def function4():
    numbers = [number for number in range(1, 1+10)]

    def with_map():
        li = list(map(lambda number: (number, number ** 2), numbers))
        print(li)

    def with_list():
        li = [(number, number ** 2) for number in numbers]
        print(li)

    with_map()
    with_list()

function4()