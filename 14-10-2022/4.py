import pandas as pd

# c = [
#     {'a': 20, 'b': 54},
#     {'a': 22, 'b': 55}
# ]
# s = pd.DataFrame(c)
# print(s)
#
# cars = [
#         {"model": "i20", "company": "hyudai", "price": 15, "fuel": "petrol"},
#         {"model": "seltos", "company": "kia", "price": 19},
#         {"model": "meridian", "company": "jeep", "price": 43}
#     ]
# cars_index = ['c1', 'c2', 'c3']
#
# df = pd.DataFrame(cars, index=cars_index)
# print(df)

# numbers = [
#     [10, 20, 30, 40, 50],
#     [60, 70, 80, 90, 100]
# ]
#
# df = pd.DataFrame(numbers, index=["r1", "r2"], columns=["col1", "col2", "col3", "col4", "col5"])
# print(df)
#
# numbers2 = [
#     [10, 20],
#     [30, 40],
#     [50, 60],
#     [70, 80],
#     [90, 100]
# ]
# df2 = pd.DataFrame(numbers2)
# print(df2)

df = pd.read_csv('Data.csv')
# print(df)

# print(df.values)
# print(df.head(8))
# df.info()
# print(df.describe())
# print(df.mean(numeric_only=True))
# print(df[['Salary', 'Country']])

df = pd.read_csv('50_Startups.csv')
# print(df)
# print(df.describe())
# df.info()
# print(df['RnD'].isna().sum())
# print(df.count())
# print(df.min())
# print(df.max())
# print(df.sum())

# print(df['Administration'].min())
# print(df['Administration'].max())
# print(df['Administration'].sum())
# print(df['Administration'].count())

# print(df['RnD'][:4])
print(df.loc[4:6, 'Administration'])
