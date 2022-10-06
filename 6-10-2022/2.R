df = read.csv('NBA.csv')
# find all the players
View(df)
# find the players playing with Team 'Boston Celtics'
View(df[df$Team == 'Boston Celtics', ])

# find salary of players having age less than 25
View(df[df$Age < 25, ])

# find the weight and height  of players earning more than 3500000
View(df[df$Salary > 3500000, c('Weight', 'Height')])

# find the players age, team and name who are playing as 'PG'
View(df[df$Position == 'PG', c('Age', "Name", "Team")])

# find the players name, team, age and salary who are using number 44
View(df[df$Number == 44, c("Name", "Number", 'Team', "Age", 'Salary')])
print(class(T))
