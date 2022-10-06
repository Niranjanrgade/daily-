average = function(...) {
  sum <- 0
  
  for (number in list(...)) {
    sum <- sum + number
  }
  
  avg <- sum / length(list(...))
  
  print(avg)
}

average(78, 79, 80, 88)
mean(c(78, 79, FALSE, 88))
 
r = as.logical('T')
print(r)
