numbers = [number for number in range(1, 1+10)]


def even():
    def number_filter(number):
        if number % 2 == 0:
            return number

    even_number = list(map(number_filter, numbers))
    even_number_a = []

    for number in even_number:
        if number != None:
            even_number_a.append(number)

    print(even_number_a)


def odd():
    def number_filter(number):
        return number % 2 != 0

    odd_numbers = list(filter(number_filter, numbers))

    print(odd_numbers)

odd()
