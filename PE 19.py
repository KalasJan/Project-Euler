# Problem 19

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import math

m = 100*12 # months
s = 7 # sunday is 1 of 7 days

ms = math.floor(m/s)

print (ms)