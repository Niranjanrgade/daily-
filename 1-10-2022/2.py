li = [number for number in range(1, 100, 5)]
tup = tuple(li)

print(li.__sizeof__())
print(tup.__sizeof__())

di = dict(name='p', age=15)

for value in di:
    print(value)

for key in di:
    print(key)

tup = 78, 74
di = {tup:'y'}
print(di)

my_set = {}
print(type(my_set))

set_2 = set("rfjnskfyiuhf")
print(set_2, len(set_2))

set_2.discard(5)
print(set_2)

set_3 = set()
print(set_3)