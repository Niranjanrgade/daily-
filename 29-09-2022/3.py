def function_squre():
    numbers = [x for x in range(65, 65 + 27)]
    squre = lambda x: x ** 2
    squres = [squre(number) for number in numbers]
    print(squres)


# function_squre()

def function4():
    numbers = [number for number in range(1, 1 + 10)]
    cube = lambda number: number ** 3

    cubes = list(map(cube, numbers))
    print(cubes)


function4()


def function5():
    temperatures = [temperature for temperature in range(90, 90 + 10 + 1)]
    convertor = lambda temperature: temperature * 1.8 + 32
    f_temperature = list(map(convertor, temperatures))

    print(f_temperature)


function5()
