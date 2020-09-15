# Problem 17

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? (and is a word)

a = (3+3+5+4+4+3+5+5+4) # numbers 1-9, 9*10+100 = 190 times
b = (3+6+6+8+8+7+7+9+8+8) # 10-19, 10 times
c = (6+6+5+5+5+7+6+6) # 20, 30, ..., 90, 10*10 = 100 times
d = 7 # hundred,  900 times
e = 3 # and, 99*9 = 891 times
f = 11 # one thousand 

print (190 * a + 10 * b + 100 * c + 900 * d + 891 * e + f)