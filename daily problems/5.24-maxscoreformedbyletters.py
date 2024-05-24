# Given a list of words, list of  single letters (might be repeating) and score of every character.

# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

# It is not necessary to use all characters in letters and each letter can only be used once.
# Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
from collections import Counter

def maxScoreWords(words, letters, score):
    def formable_word(w, lettercount):
        word_count = Counter(w)
        for c in word_count: 
            if word_count[c] > lettercount[c]: # does the count of that character ever exceed what is available?
                return False
        return True # if condition never happens

    def get_score(w):
        res = 0
        for c in w:
            res += score[ord(c) - ord('a')] # get number where letter is
        return res

    lettercount = Counter(letters) # counts occurences of each letter and converts to hashmap
    def backtrack(i):
        if i == len(words):
            return 0
        res = backtrack(i+1)# either skip the word
        if formable_word(words[i], lettercount):# or include it (when possible)
            for c in words[i]:
                lettercount[c] -= 1
            res = max(res, get_score(words[i]) + backtrack(i + 1))
            for c in words[i]:
                lettercount[c] += 1
        return res
    return backtrack(0)