def function4():
    marks = [12, 13, 8, 4, 16, 20, 13, 17, 3, 1, 2, 6]

    def passed_filter(mark):
        return mark >= 6

    passed = list(filter(passed_filter, marks))
    print(passed)
    failed = []
    for mark in marks:
        if mark not in passed:
            failed.append(mark)
    print(failed)


# function4()

persons = [
    {"name": "person1", "age": 10, "address": "pune", "email": "p1@test.com"},
    {"name": "person2", "age": 21, "address": "mumbai", "email": "p2@test.com"},
    {"name": "person3", "age": 22, "address": "karad", "email": "p3@test.com"},
    {"name": "person4", "age": 13, "address": "satara", "email": "p4@test.com"},
    {"name": "person5", "age": 24, "address": "nashik", "email": "p5@test.com"}
]


def function2():
    # def is_eligible(person):
    #     return person['age'] >= 18

    is_eligible = lambda person: person['age'] >= 18

    filtered_person = list(filter(is_eligible, persons))
    for person in filtered_person:
        print(person)


# function2()


def function3():
    # is_eligible = lambda person: person['age'] >= 18

    # filtered_person = list(filter(lambda person: person['age'] >= 18, persons))
    # filtered_names =

    print(list(map(lambda person: person['name'], filter(lambda person: person['age'] >= 18, persons)))
)


function3()