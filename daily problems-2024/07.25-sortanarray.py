# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions 
# in O(nlog(n)) time complexity and with the smallest space complexity possible.


class Solution:
    def sortArray(self, items):
        if len(items) <= 1:
            return items

        middle_index = len(items) // 2
        left_split = items[:middle_index]
        right_split = items[middle_index:]

        left_sorted = self.sortArray(left_split)
        right_sorted = self.sortArray(right_split)

        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        result = []

        while (left and right):
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        if left:
            result += left
        if right:
            result += right

        return result