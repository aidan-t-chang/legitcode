# Given a collection of candidate numbers (candidates) and a target number 
# (target), 
# find all unique combinations in candidates where the candidate 
# numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()

        res = []
        def backtrack(pos, cur, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(i+1, cur, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack(0, [], target)
        return res