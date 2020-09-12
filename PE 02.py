# Project Euler 2

# We know the Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# So we can see the sequence as L-L-S-L-L-S-L-L-S... where L is odd (lichý) and S is even (sudý)
# Now: let's x = 1, y = 1, the "new sequence" is:
# x, y, x+y, x+2y, 2x+3y, 3x+5y, 5x+8y, 8x+13y ... the coefficients are numbers of Fib. sequence
# also each 3rd member (x+y, 3x+5y, ...) is even

def F():
	x = y = 1
	sum = 0 # soucet prvnich lichych clenu je 0
	while (sum < 1000000):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
print (sum)

# pokud soucet nepresahne 1 mil., pridej soucet kx + ly, kde koeficienty k,l jsou zase z Fib. posloupnosti
