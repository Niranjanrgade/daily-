purchased = c("Yes", "No", "Yes", "Yes", "No", "No", "Yes")
T = TRUE
purchased.factor = factor(
  purchased, 
  levels = c("No", "Yes"),
  labels= c(T, F)
)
print(purchased.factor)

func = function() {
  num = 5
  print(num)
}

func()
num

