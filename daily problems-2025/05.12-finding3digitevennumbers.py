# You are given an integer array digits, where each element is a digit. The array may contain duplicates.

# You need to find all the unique integers that follow the given requirements:

# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

# Return a sorted array of the unique integers.

class Solution:
    def findEvenNumbers(self, digits):
        res = []
        for n in range(100, 1000, 2):
            numsplit = [s for s in str(n)]
            if all(numsplit.count(d) <= digits.count(int(d)) for d in numsplit):
                res.append(n)
        return sorted(res)