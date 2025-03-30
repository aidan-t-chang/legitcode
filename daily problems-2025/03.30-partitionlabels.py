# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
#
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
#
# Return a list of integers representing the size of these parts

class Solution:
    def partitionLabels(self, s: str):
        # left and right boundaries indicating where each character begins and ends
        # find the largest interval that encompasses others
        last = [0] * 26
        for i, n in enumerate(s):
            last[ord(n) - ord('a')] = i
        
        end = 0
        start = 0
        sizes = []

        for i, char in enumerate(s):
            end = max(end, last[ord(char) - ord('a')])

            if i == end:
                sizes.append(i - start + 1)
                start = i + 1
        return sizes