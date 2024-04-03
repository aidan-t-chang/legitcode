# Given two strings s and t, 
# return true if t is an anagram of s, and false otherwise.

def validAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t
print(validAnagram("anagram", "nagaram"))