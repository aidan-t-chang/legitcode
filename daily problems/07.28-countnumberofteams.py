# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or 
# (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. 
# (soldiers can be part of multiple teams).




class Solution:
    def numTeams(self, rating):
        res = 0
        for m in range(1, len(rating) - 1):
            left_smaller = right_larger = 0
            
            for i in range(m):
                if rating[i] < rating[m]:
                    left_smaller += 1
            for i in range(m+1, len(rating)):
                if rating[i] > rating[m]:
                    right_larger += 1
            res += left_smaller * right_larger # count ascend

            left_larger = m - left_smaller
            right_smaller = len(rating) - m - 1 - right_larger # how many elements are to the right of m pointer
            res += left_larger * right_smaller

        return res