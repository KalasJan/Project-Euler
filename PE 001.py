# project Euler 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# We have 3 sequences (multiples by 3, by 5 and by 15).
# So the total sum is a sum of arithmetic sequences. 
# 1st is 3* sum 1+...+333 (999/3), 2nd 1+...+199 (995/15) and 3rd sum 1+...+66 (990/15)
print (3*333*334/2+5*199*200/2-15*66*67/2)
