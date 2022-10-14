import pandas as pd

df = pd.read_csv('titanic.csv')
# print(df.columns)
# df.drop(['body'], axis=1, inplace=True)
# print(df.columns)
#
# df['extra'] = 5
# print(df.columns)
# df.to_csv('t.csv')
# # print(pd.read_csv('t.csv'))
# del df['extra']
# print(df.columns)
print(df['body'].isna().sum())
mean_body = df['body'].mean()

df['body'].fillna(mean_body, inplace=True)
print(df['body'].isna().sum())
