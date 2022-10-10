import pandas as pd

df = pd.read_csv('50_Startups.csv')
# print(df.count())
# print()
#
# print(df.min())
# print()
#
# print(df.max())
# print()
#
# print(df.sum(numeric_only=True))
# print()
#
# print(df.Administration.count())
# print()
#
# print(df.Profit.min())
# print()
#
# print(df.Profit.max())
# print()
#
# print(df.Profit.sum())
# print()

print(df.isna().sum())