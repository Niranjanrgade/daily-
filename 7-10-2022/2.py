import numpy as np


def function4():
    a1 = np.array([23, 25, 49, 60, 70, 90, 98, 67, 89])

    # [23, 25, 49]
    # use positive and boolean indexing
    print(a1[:3])
    print(a1[-9:-6])
    print(a1[-7:-10:-1])
    print(a1[[True, True, True, False, False, False, False, False, False]])

    # find out the values less than 40
    print(a1[a1 < 40])

    # find out the values greater than 35
    print(a1[a1 > 35])

    # [98, 67, 89]
    print(a1[-3:])

    # [25, 49, 60, 70]
    print(a1[1:5])

    a1[2] = 5
    print(a1)


function4()