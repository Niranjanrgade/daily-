
# create a matrix with 4x4
m5 = matrix(1:16, nrow = 4, ncol = 4)

# get the rows and columns separately

# create a matrix with 3x3
m6 = matrix(1:9, nrow = 3, ncol = 3)

# get the rows and columns separately
print(m5[1, ])
print(m5[2, ])
print(m5[3, ])
print(m5[4, ])

print(m5[,1])
print(m5[,2])
print(m5[,3])
print(m5[,4])

print(m6[1, ])
print(m6[2, ])
print(m6[3, ])

print(m6[,1])
print(m6[,2])
print(m6[,3])


# create a matrix with 3x4
m7 = matrix(1:12, nrow = 3, ncol = 4)

print(m7[1, ])
print(m7[2, ])
print(m7[3, ])

print(m7[,1])
print(m7[,2])
print(m7[,3])
print(m7[,4])


# get the rows and columns separately
m8 = matrix(1:2, 2, 2, T)
print(m8)
