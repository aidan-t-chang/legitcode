# Given an array of integers heights representing the 
# histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

def histogram(heights):
    maxA = 0
    stack = [] # pair: (index, height)
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h: # top value's height greater than our current height
            index, height = stack.pop()
            maxA = max(maxA, height * (i - index)) # width
            start = index
        stack.append((start, h))
    for i, h in stack: # able to be extended all the way to the end of the histogram
        maxA = max(maxA, h * (len(heights) - i))
    return maxA
