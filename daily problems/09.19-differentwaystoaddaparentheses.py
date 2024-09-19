# Given a string expression of numbers and operators, 
# return all possible results from computing all the different possible 
# ways to group numbers and operators. 
# You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and 
# the number of different results does not exceed 104.

class Solution:
    def diffWaysToCompute(self, expression: str):
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y
        }

        def backtrack(l, r):
            res = []

            for i in range(l, r+1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(l, i-1)
                    nums2 = backtrack(i+1, r)

                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(operations[op](n1, n2))
            if res == []:
                res.append(int(expression[l:r+1]))
            return res

        return backtrack(0, len(expression)-1)