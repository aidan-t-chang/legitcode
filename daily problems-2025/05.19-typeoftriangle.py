# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

class Solution:
    def triangleType(self, nums) -> str:
        if nums.count(nums[0]) == 3:
            return "equilateral"

        if all(nums[i] < nums[(i+1)%3] + nums[(i+2)%3] for i in range(len(nums))):
            if len(set(nums)) == 2:
                return "isosceles"
            return "scalene"

        return "none"