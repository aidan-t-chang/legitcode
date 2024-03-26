# Given a string s consisting of words and spaces, 
# return the length of the last word in the string.

def leng(s):
    w = s.split()
    return len(w[-1].strip())

print(leng('Hello World'))