# You are given two arrays with positive integers arr1 and arr2.

# A prefix of a positive integer is an integer formed by one or more of its digits, 
# starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, 
# while 234 is not.

# A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. 
# For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.

# You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs 
# to arr1 and y belongs to arr2.

# Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        prefix_map = {}
        
        # Step 1: Build the prefix map for arr1
        for num in arr1:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                prefix_map[prefix] = prefix_map.get(prefix, 0) + 1
        
        max_length = 0
        
        # Step 2: Check for common prefixes in arr2
        for num in arr2:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                if prefix in prefix_map:
                    max_length = max(max_length, len(prefix))
        
        return max_length