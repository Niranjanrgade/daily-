li = ['test'] * 5
print(li)

print((li + [number for number in range(1, 1 + 10)])[::-1])

tup = tuple([number for number in range(4, 40, 5)])

a, *b, c, d = tup

print(b)
print(c)
