# Input values
a, b, c = 1, 2, 3

# Cyclic swap: a <- c, b <- a, c <- b
a, b, c = c, a, b

print(a, b, c)  # Output: 3 1 2
