# Given a string s consisting of words and spaces, 
# return the length of the last word in the string.

def leng(s):
    w = s.split()
    gg = w[-1]
    return len(gg)

print(leng('Hello World'))