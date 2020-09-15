# Problem 6

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# (1+2+...+1000)^2 - (1^2+2^2+...+1000^2)

# a = 1+2+3+...+1000 = 1000*(1+1000)/2
# b = 1^2+2^2+...+1000^2 = 1+4+9+...+1000000 = 1000*(1000+1)*(2*1000+1)/6
# in general: 1^2 + 2^2 + .. + n^2 = n*(n+1)*(2n+1)/6

a = (1000*(1+1000)/2)**2 # (1+2...+1000)^2
b = 1000*(1000+1)*(2*1000+1)/6 # 1^2 + 2^2 + ... + 1000^2

print ("result is", str(int(a-b)))