import pandas as pd
from matplotlib import markers, pyplot as plt

#
df = pd.read_csv('Data.csv')
#
# x = df['Age'].sort_values()
# y = df['Salary']
#
# plt.plot(x, y, color='g')
# plt.grid()
# plt.show()

# se = pd.Series([n for n in range(5)], index=[a for a in range(5, 10)])
# print(se)

# print(df.loc[2:5])

# df.info()

# print(df.to_string())

# for x in df.index:
#     print(x)

del df['Country']

df.drop(['Purchased'], axis= 1, inplace=True)
# print(df)
print(df.corr())
df.plot()
plt.show()