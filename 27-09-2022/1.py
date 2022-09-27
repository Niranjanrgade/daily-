def f1():
    f2()
    print()


def f2():
    f1()
    print()


f1()
f2()