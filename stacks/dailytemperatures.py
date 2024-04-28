# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the 
# number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

def daily(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for index, temps in enumerate(temperatues): # index and value at the same time
        while stack and temps > stack[-1][0]:
            stackt, stacki = stack.pop()
            res[stacki] = (stack - stacki)
        stack.append([temps, stack])
    return res
