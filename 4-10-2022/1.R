l2 = list(
  c(20, 40, 60, 80, 100),
  c("i20", 'i10', 'nano', 'sonet', 'seltos', 'meridian'),
  c('steve jobs', 'bill gates', 'bill joy'),
  c('apple', 'hp', 'microsoft', 'red hat')
)

print(l2)
print(l2[[1]])
print(l2[[2]])
print(l2[[3]])
print(l2[[4]])
print(l2[[2]][1])
print(l2[[2]][6])
print(l2[[1]][4])
print(l2[[1]][2])
print(l2[[2]][3])
print(l2[[3]][3])

l4 = list(
  number=c(20, 40, 60, 80, 100),
  model=c("i20", 'i10', 'nano', 'sonet', 'seltos', 'meridian'),
  person=c('steve jobs', 'bill gates', 'bill joy'),
  company=c('apple', 'hp', 'microsoft', 'red hat')
)
print(l4)
print(l4$number)
print(l4$model)
print(l4$person)
print(l4$company)
print(l4$model[1])
print(l4$model[6])
print(l4$number[4])
print(l4$number[2])
print(l4$model[3])
print(l4$person[3])

