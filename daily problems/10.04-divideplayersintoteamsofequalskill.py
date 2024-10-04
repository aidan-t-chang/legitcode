# You are given a positive integer array skill of even length n where 
# skill[i] denotes the skill of the ith player. Divide the players into 
# n / 2 teams of size 2 such that the total skill of each team is equal.

# The chemistry of a team is equal to the product of the skills of the
# players on that team.

# Return the sum of the chemistry of all the teams, or return -1 if 
# there is no way to divide the players into teams such that the total 
# skill of each team is equal.


class Solution:
    def dividePlayers(self, skill) -> int:
        skill.sort()

        summ = skill[0] + skill[-1]

        l, r = 0, len(skill) - 1

        res = 0

        while l < r:
            if skill[l] + skill[r] != summ:
                return -1
            res += (skill[l] * skill[r])
            l += 1
            r -= 1

        return res