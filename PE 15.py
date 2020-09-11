# Project Euler 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# if we use a paper, it's easy
# in m*n grid there are (m+n)! / (m! * n!)

from math import factorial
print ((factorial(20+20))/(factorial(20)*factorial(20)))

# also we can use a definition of factorial

def factorial(x):
    if x<=1:
        return 1
    else:
        return x * factorial(x-1)
    
print (factorial(20+20)/(factorial(20)*factorial(20)))