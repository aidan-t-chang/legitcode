# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumsq = 0
a = 100

for n in range(1, a+1):
    sumsq += n**2
    
sum = 0
for n in range(1, a+1):
    sum += n

print(sum**2 - sumsq)