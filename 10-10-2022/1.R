genre <- factor(c('j', 'r', 'c', 'c', 'p', 'j', 'r', 'j'), 
                levels = c('c', 'j', 'p', 'r', 'o'))
genre
levels(genre)
genre[2] <- 'n' 
genre

plot(seq(from=3, to=61, by=3), main="g", 
     xlab = "x", ylab='y')
