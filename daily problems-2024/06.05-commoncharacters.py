# Given a string array words, 
# return an array of all characters that show up in all strings within the words 
# (including duplicates). You may return the answer in any order.

from collections import Counter

class Solution:
    def commonChars(self, words):
        cnt = Counter(words[0]) # returns a hashmap of the count of every letter
        #similar to defaultdict

        # get the count of every character we want in the output
        for w in words:
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])


        res = []
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)
        return res
