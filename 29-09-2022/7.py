numbers = [number for number in range(1, 1 + 10)]


def function1():
    even_number_squares = [number ** 2 for number in numbers if number % 2 == 0]

    print(even_number_squares)


function1()


def function2():
    even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
    squares = list(map(lambda number: number ** 2, even_numbers))

    print(squares)


function2()
