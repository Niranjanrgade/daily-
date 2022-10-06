library(tidyverse)
head(diamonds)
glimpse(diamonds)
str(diamonds)
summary(diamonds)
summarise(diamonds)
ggplot(data = diamonds, aes(x = carat, y = price, color = cut)) + geom_point()
 