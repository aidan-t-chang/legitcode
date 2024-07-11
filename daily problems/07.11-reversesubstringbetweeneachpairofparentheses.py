# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, 
# starting from the innermost one.

# Your result should not contain any brackets.



#first one doesnt work: how?
def reverseParentheses(s: str) -> str:
    istack = []
    for i in range(len(s)):
        print(i, s[i])
        if s[i] == "(":
            istack.append(i)
        elif s[i] == ")":
            rev = istack.pop()
            s = s.replace(s[rev:i+1], s[rev:i+1][::-1])
    s = s.replace('(', '')
    s = s.replace(')', '')
    return s

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []  # Stack to hold intermediate strings
        ans = ""  # String to build the current result

        for ch in s:
            if ch == '(':
                # Push the current string to the stack and start a new one
                stack.append(ans)
                ans = ""
            elif ch == ')':
                # Reverse the current string
                ans = ans[::-1]
                # Concatenate with the string on top of the stack
                ans = stack.pop() + ans
            else:
                # Append regular characters to the current string
                ans += ch

        return ans  # Return the final result