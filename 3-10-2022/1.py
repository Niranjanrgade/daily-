numbers = [number for number in range(0, 11)]

li = [number + 20 for number in range(0, 11)]
print(li)

li2 = list(map(lambda number: number + 20,numbers))
print(li2)