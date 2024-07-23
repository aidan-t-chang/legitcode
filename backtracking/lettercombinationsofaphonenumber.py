# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. 
# Return the answer in any order.


class Solution:
    def letterCombinations(self, digits):
        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        def backtrack(i, cur):
            if len(digits) == len(cur):
                res.append(cur)
                return
            
            for c in table[digits[i]]:
                backtrack(i+1, cur + c)
            
        if digits:
            backtrack(0, "")
        return res