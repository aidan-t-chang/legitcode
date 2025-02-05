# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count_diff = 0

        check1 = [char for char in s1]
        check2 = [char for char in s2]

        check1.sort()
        check2.sort()
        if check1 != check2:
            return False



        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count_diff += 1
                if count_diff > 2:
                    return False

        return count_diff == 2 or count_diff == 0