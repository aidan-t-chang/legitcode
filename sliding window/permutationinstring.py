# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

def perms(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1C, s2C = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1C[ord(s1[i]) - ord('a')] += 1
        s2C[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += 1 if s1C[i] == s2C[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: # there is a permutation
            return True
        
        index = ord(s2[r]) - ord('a')
        s2C[index] += 1
        if s1C[index] == s2C[index]:
            matches += 1
        elif s1C[index] + 1 == s2C[index]: # they WERE exactly equal
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2C[index] -= 1
        if s1C[index] == s2C[index]:
            matches += 1
        elif s1C[index] - 1 == s2C[index]: # they WERE exactly equal
            matches -= 1
        l += 1
    return matches == 26