# problem 4

# Find the largest palindrome made from the product of two 3-digit numbers.

for x in range (900, 1000): # we want to have biggest nubmer - so we use interval 900 - 999
    for y in range (900, 1000):
        n = x*y
        if str(n) == str(n)[::-1]: # definition of palindromes
            print (n)
            # we have 12 solution, we choose the biggist of them