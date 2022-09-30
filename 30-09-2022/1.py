# numbers = [number for number in range(1, 1+10)]
# li = []
# for number in numbers:
#     if number % 2 == 0:
#         li.append("Even")
#     else:
#         li.append("Odd")
#
# print(li)
#
# li2 = ['Even' if number % 2 == 0 else 'Odd' for number in numbers ]
# print(li2)
#
#
# def checker(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return 'Odd'
#
#
# li3 = list(map(checker, numbers))
#
# print(li3)
#
# print('even') if 6 % 2 == 0 else print('odd')

def function2():
    marks = [10, 2, 4, 5, 8, 9, 14, 18, 17, 18]

    # marks > 6 => passed or failed
    # ['PASSED','FAILED', .... ]

    result = ['passed' if mark > 6 else 'failed' for mark in marks]
    print(result)

    result2 = list(map(lambda mark: 'passed' if mark > 6 else 'failed', marks))
    print(result2)

function2()

