# Given the binary representation of an integer as a string s, 
# return the number of steps to reduce it to 1 under the following rules:

# If the current number is even, you have to divide it by 2.

# If the current number is odd, you have to add 1 to it.

# It is guaranteed that you can always reach one for all test cases.

 
class Solution:
    def numSteps(self, s):
        res = 0
        carry = 0
        for i in reversed(range(1, len(s))):  # dont operate on the last value
            digit = (int(s[i]) + carry) % 2
            if digit == 0:
                res += 1
            else:
                carry = 1
                res += 2
        
        return res + carry