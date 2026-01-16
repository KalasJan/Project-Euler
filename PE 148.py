# Project Euler, 148
# we have a Pascal's triangle
# how many nubers in 10**9 rows are not divisible by 7?

# base 7
def base7(n):
    digits = []
    while n >0:
        digits.append(n % 7)
        n //= 7
    return digits[::-1]

# total count
def total(k):
    digits = base7(k)
    long = len(digits)
    
    count = 0
    mult = 1
    
    for i in range (long):
        d = digits[i]
        
        rem = long - i - 1
        
        for a in range(d):
            count += mult*(a+1)*(28**rem)
            # 28 = 1+2+..+7
            # mult = multiple (n_p + ) for p in (0, k-1)
        mult *= (d+1)
    return count

print (total(10**9))