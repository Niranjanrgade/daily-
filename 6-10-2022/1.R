df = read.csv('Data.csv')
View(df)
colnames(df)
row.names(df)
nrow(df)
ncol(df)
summary(df)
str(df)
class(df)
print(df[1:5, c(1, 3)])
print(df[df$Purchased == 'Yes', ])
print(df[df$Salary > 75000, 1])
print(df[df$Salary > 75000, 2])
print(df[df$Purchased == 'No', 2:3])
