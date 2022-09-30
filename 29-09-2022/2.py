def execute2(p1, p2, function):
    print(function(p1, p2))


p1 = 10
p2 = 5

execute2(p1, p2, lambda p1, p2: p1 + p2)
execute2(p1, p2, lambda p1, p2: p1 - p2)
execute2(p1, p2, lambda p1, p2: p1 * p2)
execute2(p1, p2, lambda p1, p2: p1 / p2)