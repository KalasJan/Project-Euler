# project Euler, 340

# a, b, c are integer
# f(n) = n-c, n>b
# f(n) = f(a+f(a+f(a+f(a+n)))), n<= b
# S (a,b,c) = sum f(n) for n = 0 .. b
# last 9 digits of S(21**7, 7**21, 12**7) ?

# math help: https://www.ivl-projecteuler.com/overview-of-problems/30-difficulty/problem-340

from math import floor as fl

a = 21**7
b = 7**21
c = 12**7

mod = 10**9 # I want last 9 digits

def f(n):
    if  n > b:
        return n - c
    else:
        return 8*a+n-7*c
    # = f(a+f(a+f(a+f(a+n))))
    # f(a+n) = 5a+n-4c
    
fr = fl(b/a)

suma1 = (b*(b+1))//2

suma2 = ((fr-1)*fr)//2 * (4*a**2 - 3*a*c)
suma3 = 4*a*fr*(a-c)

suma4 = (b-a*fr+1)*(4*a*(fr+1)-(3*fr+4)*c)

total = suma1 + suma2 + suma3 + suma4
result = total % mod

print(result)