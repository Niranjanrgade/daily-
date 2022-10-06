df = read.csv('50_Startups.csv')
print(df)
head(df, 10)
tail(df, 10)
colnames(df)
nrow(df)
ncol(df)
summary(df)
str(df)
print(df[c("Administration", 'Marketing')])
print(df[c('Marketing', "Profit", 'RnD')])
df[df['Marketing'] > 550000]

         