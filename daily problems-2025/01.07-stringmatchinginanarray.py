# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string


class Solution:
    def stringMatching(self, words):
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j] and words[i] in words[j] and words[i] not in res:
                    res.append(words[i])

        return res