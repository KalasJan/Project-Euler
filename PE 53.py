# Problem 53

from math import factorial

def C(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))

total = 0
for n in range (1, 101):
    for r in range (1, n+1):
        if C(n, r) >= 10**6:
            total +=1
            print (total)