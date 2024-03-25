# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

def pal(x):
    if x < 0:
        return False
    lis = [int(digit) for digit in str(x)]
    if lis == lis[::-1]:
        return True
    else:
        return False

def pal2(x):
    x = str(x)
    return x == x[::-1]

print(pal2(-121))
print(pal2(14))
print(pal2(1415141))