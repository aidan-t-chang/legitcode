# Given a list of 24-hour clock time points in "HH:MM" format, 
# return the minimum minutes difference between any two time-points in the list.

class Solution(object):
    def findMinDifference(self, timePoints):
        # Convert times to minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
        
        # Sort times in ascending order
        minutes.sort()
        
        # Find minimum difference across adjacent elements
        min_diff = float('inf')
        for i in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[i + 1] - minutes[i])
        
        # Consider the circular difference between last and first element
        min_diff = min(min_diff, 24 * 60 - minutes[-1] + minutes[0])
        
        return min_diff