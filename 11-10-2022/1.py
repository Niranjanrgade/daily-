def average(numbers_li):
    sum_of = 0

    for number in numbers_li:
        sum_of += number

    avg = sum_of / len(numbers_li)
    return avg


def mode(numbers_li):
    di = {}

    for number in numbers_li:
        if di.get(number) is None:
            di[number] = 1
        else:
            di[number] += 1

    li = list(di.values())
    li.sort()
    print(li)
    index = li[-1]

    return di[index]


def median(numbers_li):
    numbers_li.sort()
    print(numbers_li)
    if len(numbers_li) % 2 == 0:
        print(numbers_li[int(len(numbers_li) / 2) -1])
        print(numbers_li[int(len(numbers_li) / 2)])
        median_of_numbers = (numbers_li[int(len(numbers_li) / 2) - 1] + numbers_li[int(len(numbers_li) / 2)]) / 2
        return median_of_numbers

    else:
        return numbers_li[int(len(numbers_li) / 2)]


numbers = [5, 84, 6, 1, 8]
# print(average(numbers))
print(median(numbers))
# print(mode(numbers))
