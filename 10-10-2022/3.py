import pandas as pd

df = pd.read_csv('Data.csv')

print(type(df['Salary']))

# print(type(df[['Salary', 'Country']]))

# print(df.Salary, df.Country)

print(df.sum(numeric_only=True))

# df = pd.read_csv('titanic.csv')
#
# print(df.body.isna().sum())
# df.dropna()
# print(df.body.isna().sum())
