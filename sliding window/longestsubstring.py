# Given a string s, find the length of the longest 
# substring without repeating characters.

def find(s):
    chars = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in chars: # there is a duplicate in the character set, must update window
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        res = max(res, r - l + 1)
    return res