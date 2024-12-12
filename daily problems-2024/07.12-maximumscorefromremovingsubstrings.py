# You are given a string s and two integers x and y. 
# You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

class Solution:
    def maximumGain(self, s, x, y):
        def remove_pairs(pair, score):
            # updates s and removes pairs
            nonlocal s
            rev = 0
            stack = []
            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    rev += score
                else:
                    stack.append(c)
            s = "".join(stack) # joins all the strings together
            return rev
        
        res = 0
        pair = "ab" if x > y else "ba"
        res += remove_pairs(pair, max(x, y)) # already found the max above
        res += remove_pairs(pair[::-1], min(x, y))
        return res