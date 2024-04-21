# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

def trap(height):
    if not height:
        return 0
    L, R = 0, len(height) - 1
    maxL, maxR = height[L], height[R]
    rainamount = 0

    while L < R:
        if maxL < maxR:
            L += 1
            maxL = max(maxL, height[L])
            rainamount += maxL - height[L]
        else:
            R -= 1
            maxR = max(maxR, height[R])
            rainamount += maxR - height[R]
    return rainamount