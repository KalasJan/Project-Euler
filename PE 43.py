# Problem 43

from itertools import permutations

d = permutations("0123456789")

count = 0

for p in d:
    if (int("".join(p[1:4])) % 2 == 0 and
        int("".join(p[2:5])) % 3 == 0 and
        int("".join(p[3:6])) % 5 == 0 and
        int("".join(p[4:7])) % 7 == 0 and
        int("".join(p[5:8])) % 11 == 0 and
        int("".join(p[6:9])) % 13 == 0 and
        int("".join(p[7:10])) % 17 == 0):
        count += int("".join(p))
        
        print (count)