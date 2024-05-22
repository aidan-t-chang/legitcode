# Given two strings s and t of lengths m and n respectively, return the minimum window substring
# of s such that every character in t 
# (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

def findmin(s, t):
    if t == "":
        return ""
        
    countT, window = {}, {}

    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resl = [-1, -1], float('infinity')
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1 # just satisfied one condition
        
        while have == need:
            if (r - l + 1) < resl: # size of current window 
                res = [l, r]
                resl = r - l + 1
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if resl != float('infinity') else ""