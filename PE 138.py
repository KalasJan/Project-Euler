# Problem 138

# mame rovnoramenny trojuhelnik o zakladne b, vyskou h a rameny L
# plati h = b+-1
# najdete soucet 12 nejmensich hodnot L 

# way 1

from itertools import islice

# pythagorean triplet
def Triangle(k, l):
    h = k * l
    b = (l ** 2 - k ** 2) // 2
    L = (l ** 2 + k ** 2) // 2
    return (h, b, L)
   
# fibonacci sequence
def fib():
    a1 = 1
    a2 = 1
    while True:
        for a in range(3):
            a1, a2 = (a2, a1 + a2)
        yield (a1, a2)

# total sum
if __name__ == '__main__':
    result = 0
    for h, b, L in (Triangle(k, l) for k, l in islice(fib(), 12)):
        d = 1
        while abs(((b * d) * 2) - (h * d)) != 1:
            d += 1
        result += L * d
    print(result)
    
# Way 2:
    
def Fibonacci(n):
    if n<0:
        print("False")
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print (sum(Fibonacci(6*n+3)/2 for n in range (1, 13)))