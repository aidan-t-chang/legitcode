# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?


i = 2520
list = [11, 12, 13, 14, 16, 17, 18, 19, 20]
def solver(i):
    for num1 in range(2520, 999999999, 2520):
        if all(num1 % num == 0 for num in list):
            return num1
    return None
        
print(solver(i))
