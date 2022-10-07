import pandas as pd

s1 = pd.Series([n * 10 for n in range(1, 1 + 10)])

s2 = pd.Series(tuple([n * 10 for n in range(1, 1 + 10)]))
print(s2)

index_ = ['model', 'company', 'price']
values = ['iphone', 'Apple', 140000]
s3 = pd.Series(values, index=index_)
print(s3)

s4 = pd.Series([23, 45, 29, 30, 10, 29, 19, 38])

# positive indexing

# negative indexing
# print(s4[-2])

# slicing
print(s4[-2:-8:-2])

# filtering
print(s4[s4 > 20])
print(s4[s4 < 23])
print(s4[s4 % 2 == 0])

