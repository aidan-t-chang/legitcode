# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def plusone(digits):
    exponent = 0
    inte = 0
    for i in digits[::-1]:
        inte += i * (10**exponent)
        exponent += 1
    splitagain = [int(n) for n in str(inte+1)]
    return splitagain

print(plusone([1,2,3]))
print(plusone([9]))
    