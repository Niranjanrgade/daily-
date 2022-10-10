import numpy as np
import pandas as pd
# di = {'a': 10}
# di2 = {'a': 10}
# di3 = {'a': 10}
#
# li = [4, 4]
# li2 = [7, 8]
# cars = [di = {'a': 10},
#         di2 = {'a': 10},
#         di3 = {'a': 10}]
#
#
# d = [li, li2]
# df = pd.DataFrame(cars)
#
# print(df)

arr = np.arange(8)
arr2 = np.reshape(arr, newshape=(2,4), order='C')
arr3 = np.reshape(arr, newshape=(2,4), order='F')
print(arr2)
print(arr3)