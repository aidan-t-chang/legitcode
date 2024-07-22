# You are given an array of strings names, 
# and an array heights that consists of distinct positive integers. 
# Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and 
# height of the ith person.

# Return names sorted in descending order by the people's heights.

class Solution:
    def sortPeople(self, names, heights):
        res = []
        num = {}

        i = 0
        for h in heights:
            num[h] = i
            i += 1

        heights.sort(reverse = True)

        for height in heights:
            res.append(names[num[height]])
        
        return res