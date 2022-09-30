def function1():
    numbers = [number for number in range(1, 1+10)]
    sum = 0
    for number in numbers:
        sum += number
    print(sum)

# function1()


def function3():
    c_temps = [c_temp for c_temp in range(90, 90 + 10)]
    f_temps = [(c_temp - 32) * 5 / 9 for c_temp in c_temps]
    print(f_temps)

function3()