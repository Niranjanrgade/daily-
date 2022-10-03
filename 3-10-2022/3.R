numbers = c(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print(numbers[c(2, 4, 6)])
print(numbers[c(1, 5, 6, 9)])
print(numbers[c(9, 10, 2, 3)])
print(numbers[c(2, 5, 3, 6)])
print(numbers[-3])
print(numbers[c(-1, -5)])

print(numbers[c(-1, -3, -5, -7, -8, -9, -10)])
print(numbers[c(-2, -3, -4, -7, -8, -10)])
print(numbers[c(-1, -4, -5, -6, -7, -8, -9)])
print(numbers[c(-1, -4, -7, -8, -9, -10)])

range(c(1, 8))

print(numbers[2:6])
print(numbers[6:10])
print(numbers[5:8])

for (index in 1:length(numbers)) {
  print(paste0(numbers[index]))
}






