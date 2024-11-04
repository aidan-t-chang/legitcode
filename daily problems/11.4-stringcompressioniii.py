# Given a string word, compress it using the following algorithm:

# Begin with an empty string comp. While word is not empty, use the following operation:
# Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
# Append the length of the prefix followed by c to comp.
# Return the string comp.

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        cur = word[0]
        count = 1

        for i in range(1, len(word)):
            if word[i] == cur and count < 9:
                count += 1
            else:
                temp = str(count) + cur
                comp += temp
                cur = word[i]
                count = 1
        
        t = str(count) + cur
        comp += t
        return comp