import numpy as np
li = [10, 20]
arr = np.array(li)
print(arr)

arr2 = np.array([number for number in range(6)])
print(arr2)

arr3 = arr2.reshape([3, 2])
print(arr3)

arr4 = arr3.reshape([2, 3])

print(arr4)


def fun():
    arr1 = np.random.random(10)
    print(arr1)

    arr2 = np.random.randint(0, 9, [4, 5])
    print(arr2)

    arr3 = np.arange(10).reshape(2, 5)
    print(arr3)

    a4 = arr3.reshape(5, 2)
    print(a4)


fun()