# PE 63

# najdete  n-ciferne cislo, ktere je n-tou mocninou.

n = 0
for a in range (1, 100):
    for b in range (1, 100):
        x = a**b
        if len(str(x)) == b:
            n = n+1
print (n)