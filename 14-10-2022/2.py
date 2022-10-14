import pandas as pd

# arr = pd.Series([n*10 for n in range(1, 6, 2)])
# print(arr)
# print(type(arr))
# print(arr.dtype)
# print(arr.ndim)
# print(arr.itemsize)
# print(sys.getsizeof(arr[0]))
# print(arr.size)
# print(arr.shape)
# print(arr.nbytes)
# print(arr.index)
# print(arr[-1])
s1 = pd.Series([23, 45, 29, 30, 10, 29, 19, 38])
# positive indexing
# print(s1[[0, 2, 4]])
    # get the values at index 0, 2, 4, and 6

# print(s1[100])
    # get the value at 100th position

    # negative indexing
# print(s1[[-1, -4]])
    # get the values at index -1, -4, -5, -7
    # get the value at -100th position
# slicing
# print(s1[2:(2+4)])
# [29, 30, 10, 29]
# [23, 45, 29, 30]
print(s1[-4:])
# [29, 19, 38]

# filtering
# print(s1[s1>20])
# find the values greater than 20
# print(s1[s1<25])

# find the values less than 23