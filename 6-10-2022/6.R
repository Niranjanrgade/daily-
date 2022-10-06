df = read.csv('Data.csv')
view(df)
select(df, Salary > 50000, everything())
