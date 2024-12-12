# You are given a string s consisting only of uppercase English letters.

# You can apply some operations to this string where, in one operation, 
# you can remove any occurrence of one of the substrings "AB" or "CD" from s.

# Return the minimum possible length of the resulting string that you can obtain.

# Note that the string concatenates after removing the substring and could 
# produce new "AB" or "CD" substrings.

class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if stack and char == "D" and stack[-1] == "C":
                    stack.pop() # remove "C"
                elif stack and char == "B" and stack[-1] == "A":
                    stack.pop() # remove "A"
                else:
                    stack.append(char)
                
        return len(stack)
