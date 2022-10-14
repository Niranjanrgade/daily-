import numpy as np
import sys

li = [n*10 for n in range(1, 6)]
arr = np.array(li, dtype=np.int64)
# print(arr)
# print(type(arr))
# print(arr.dtype)
# print(arr.ndim)
# print(arr.itemsize)
# # print(sys.getsizeof(arr[0]))
# print(arr.size)
# print(arr.shape)
# print(arr.nbytes)

# arr = np.arange(1, -12, 3)
# print(arr)
a = np.ones((3, 4), dtype=int)
# print(a)
# a = np.ones([3, 4], dtype=int)
# print(a)
# b =np.random.randint(0, 15, (2,3))
# print(b)

print(arr != 5)
print(arr[-2])
print(arr[[2, 4]])
print(arr[2:9])
print(arr[arr > 30])
