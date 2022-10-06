library(tidyverse)
install.packages('stringi')
df = read.csv('Data.csv')

print(select(df, Salary:Country, Purchased))
view(df)

view(select(starwars, height, mass, everything()))
view(starwars)

df = read.csv('Data.csv')
print(df[df$Salary > 50000 & df$Country == 'France', ])
print(df[df$Salary > 50000 | df$Country == 'Spain', ])

filter(df, Salary > 50000 & Country == 'France')
filter(df, Salary > 50000 | Country == 'Spain')
