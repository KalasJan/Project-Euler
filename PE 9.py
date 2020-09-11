# Project Euler 9

# We have 3 natural numbers a, b, c
# a**2 + b**2 = c**2
# if a+b+c = 1000, a*b*c = ?

for a in range (1, 1000):
    for b in range (1, 1000):
        c = 1000 - a - b # because a+b+c = 1000
        if a**2 + b**2 == c**2: # because Pythagorean triplet
            print ("a=", a)
            print ("b=", b)
            print ("c=", c)
            print ("abc=", a*b*c)
# there are 2 solutions
# 1st solution has a<b, 2nd has b<a, but the product  abc is the same.