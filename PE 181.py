# Project Euler 181

from functools import lru_cache

def groups(B, W):
    @lru_cache(None)  # speeds up counting by caching results
    def recursion (b, w, last_b, last_w):
        # b, w - number of black and white objects still remaining
        # last - size of the last group chosen
        if b == 0 and w == 0:
            return 1
        
        total = 0
        for i in range (0, b+1): # number of black objects in the next group
            for j in range (0, w+1): #number of white objects in the next group
                if i == 0 and j == 0:
                    continue
                
                if (i, j) < (last_b, last_w): # ensure groups are in canonical order
                    continue
                
                if i <= b and j <= w:
                    total += recursion(b - i, w - j, i, j)

        return total

    return recursion(B, W, 0, 0)

print (groups(60, 40))