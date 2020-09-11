# Project Euler 3

# What is the largest prime factor of the number 600851475143?

# In Scilab, it is so easy, the code there is:
# max(factor(600851475143)) 

import math
def max_factor(n):
   factor = 2
   while factor ** 2 <= n: # exist idea about fact.^ 2 < n (n is our number)
       while n % factor == 0: # mod (fact) = 0
           n /= factor
       factor += 1
   if (n > 1):
        return n
   return factor
print (math.floor(max_factor(600851475143)))

# math.floor - no decimal number