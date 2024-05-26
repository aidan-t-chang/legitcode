# Given a string s and a dictionary of strings wordDict, 
# add spaces in s to construct a sentence where each word is a valid dictionary word. 
# Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

def wordBreak(s, wordDict):
    wordDict = set(wordDict)
    cache = {}
    def backtrack(i):
        if i == len(s):
            return ['']
        if i in cache:
            return cache[i]
        
        res = []

        for j in range(i, len(s)):
            w = s[i:j+1]
            if w in wordDict:
                continue # prevent unnecessary nesting
            strings = backtrack(j + 1)
            if not strings:
                pass # nothing for us to do in the loop. if it doesnt execute, it has real words or empty string
            for substring in strings:
                sentence = w # sentence is the current word we started with
                if substring: # if the substring is not empty
                    sentence += " " + substring # only add spaces to the string if it is not empty
                res.append(sentence)
        cache[i] = res
        return res

    return backtrack(0)