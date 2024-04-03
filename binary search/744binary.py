# You are given an array of characters letters that is sorted in 
# non-decreasing order, and a character target. 
# There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically 
# greater than target. If such a character does not exist, 
# return the first character in letters.
# version2 the one that works

import bisect

def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters)
    o = ord(target)
    while left <= right:
        mid = (left + right) // 2
        if target not in letters:
            return letters[0]
        if o == ord(mid):
            return mid
        if o < ord(mid):
            right = mid
        if o > ord(mid):
            left = mid + 1
    return left

def version2(letters, target):
    i = bisect.bisect_right(letters, target)
    if i < len(letters):
        return i
    else:
        return letters[0]