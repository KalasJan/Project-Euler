# PE 56
# a, b < 100
# a^b s nejvetsim cifernym souctem

def cifernysoucet(n): # definujeme ciferny soucet
    return sum(map(int, str(n)))

maximalnisoucet = 0 
for a in range (1, 100):
    for b in range (1, 100): # podminky am b
        soucet = cifernysoucet(str(a**b)) 
        if soucet > maximalnisoucet:
            maximalnisoucet = soucet # chceme maximalni soucet
            
print (maximalnisoucet)