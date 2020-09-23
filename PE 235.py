# Problem 235

# u(k) = (900-3k)*r^(k-1)
# s(n) = sum (u(k)) for k = 1..n

# s(5000) = -6*10^11, r=? (12 decimal points)

# solve:
# -6 * 10**11 = sum ((900-3k)*r^(k-1)) for k = 1..5000

def u(k):
    return (900-3*k)*r**(k-1)

dolni = 1.001
horni = 1.003 # horni a dolni odhady r
zaokr = 10**(-13) # chceme 12 deset. mist
soucet = -6 * 10**11

while (horni - dolni) > zaokr:
    r = (horni + dolni) / 2
    s = sum (u(k) for k in range (1, 5001))
    if s < soucet:
        horni = r
    else:
        dolni = r
        
print (r)
    