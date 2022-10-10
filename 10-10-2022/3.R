#dt <- rep(c('y', 'n', 'y', 'n'), times = 78)

#dt

numbers <- 1:10
numbers <- seq(from=5, to=40, by=3)
numbers

35 %in% numbers
55 %in% numbers
numbers[3:8]

for (number in numbers) {
  print(number)
}