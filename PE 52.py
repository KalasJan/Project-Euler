# problem 52
# najdete nejmensi cislo, ktere obsahuje stejne cislice v x, 2x, 3x, 4x, 5x, 6x

# Manualne:
# musi to byt cast 1/7 (ale radsi se to overi)
print ("1/7=", 1/7)
print ("2/7=", 2/7)
print ("3/7=", 3/7)
print ("4/7=", 4/7)
print ("5/7=", 5/7)
print ("6/7=", 6/7)
print ("7/7=", 7/7)

# kodem

for x in range (1, 10**6):
    if set(list(str(x))) == set(list(str(2*x))) == set(list(str(3*x))) == set(list(str(4*x))) == set(list(str(5*x))) == set(list(str(6*x))):
        print (x)