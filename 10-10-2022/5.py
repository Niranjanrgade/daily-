import pandas as pd

# df = pd.read_csv('50_Startups.csv')

# print(df.iloc[0:10, 0:3])
# print(df.loc['State'])
# print(df.iloc[-10:])

df = pd.read_csv('nba.csv')

print(df.columns)

del df['College']
print(df.columns)

del df['Name']
print(df.columns)

del df['Team']
print(df.columns)

mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)
df['Bonus'] = 15000
df['NewSalary'] = df['Bonus'] + df['Salary']

mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)

df.to_csv('new_nba.csv')


