# There are n cars going to the same destination along a one-lane road. 
# The destination is target miles away.
# You are given two integer array position and speed, 
# both of length n, 
# where position[i] is the position of the ith car and 
# speed[i] is the speed of the ith car (in miles per hour).

# Return the number of car fleets that will arrive at the destination.

def carFleet(target, position, speed):
    pair = [[p,s] for p, s in zip(position, speed)]

    stack = []
    for p, s in sorted(pair)[::-1]: # reverse sorted order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]: 
        # the time taken to reach destination in the first value is less than the second value (right to left)
        stack.pop()

    return len(stack)