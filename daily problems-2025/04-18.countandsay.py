""" The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence. """

class Solution:
    def countAndSay(self, n: int) -> str:
        def compress(num):
            res = ""
            l = 0
            r = 1
            while r < len(num):
                if num[l] != num[r]:
                    res += (str((r - l)) + num[l])
                    l = r
                r += 1
            if r != l:
                res += (str((r - l)) + num[l])
            return res
            
        dp = ["1"]
        for i in range(1, n):
            dp.append(compress(dp[-1]))
        return dp[-1]