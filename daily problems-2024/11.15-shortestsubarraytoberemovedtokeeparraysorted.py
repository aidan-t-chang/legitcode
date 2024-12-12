# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

# Return the length of the shortest subarray to remove.

# A subarray is a contiguous subsequence of the array


class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:
        N = len(arr)

        r = N - 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1

        res = r

        l = 0
        while l + 1 < N and arr[l+1] >= arr[l]:
            l += 1
        res  = min (res, N - 1 - l)

        l, r = 0, N - 1

        while l < r:
            while r < N and l + 1 < r and arr[r - 1] <= arr[r] and arr[l] <= arr[r]:
                r -= 1

            while r < N and arr[l] > arr[r]:
                r += 1    
            res = min(res, r - l - 1)
            if arr[l] > arr[l+1]:
                break
            l += 1
        return res