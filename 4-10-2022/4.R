path = "C:\Users\Niranjan R Gade\Desktop\Salary_Data.csv"
df = read.csv(path)
print(df)
class(df)

df = df[c('Salary')]
print(df)

