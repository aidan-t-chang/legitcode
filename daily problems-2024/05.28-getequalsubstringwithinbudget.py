# You are given two strings s and t of the same length and an integer maxCost.

# You want to change s to t. 
# Changing the ith character of s to ith character of t costs |s[i] - t[i]| 
# (i.e., the absolute difference between the ASCII values of the characters).
# Return the maximum length of a substring of s that can be changed 
# to be the same as the corresponding substring of t with a cost less than 
# or equal to maxCost. If there is no substring from s that can be changed to 
# its corresponding substring from t, return 0.

def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    totalCost = 0
    l = 0
    res = 0

    for r in range(len(s)):
        totalCost += abs(ord(s[r]) - ord(t[r])) # total cost of current window

        while totalCost > maxCost: # move the left pointer if cost is too much
            totalCost -= abs(ord(s[l]) - ord(t[l]))
            l += 1

        res = max(res, r - l + 1) # compute the size of a substring from two pointers
    return res