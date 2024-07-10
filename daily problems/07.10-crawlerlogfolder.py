# The Leetcode file system keeps a log each time some user performs a change folder operation.

# The operations are described below:

# "../" : Move to the parent folder of the current folder. 
# (If you are already in the main folder, remain in the same folder).
# "./" : Remain in the same folder.
# "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
# You are given a list of strings logs where logs[i] is the 
# operation performed by the user at the ith step.

# The file system starts in the main folder, then the operations in logs are performed.

# Return the minimum number of operations needed to go back to the 
# main folder after the change folder operations.

class Solution:
    def minOperations(self, logs):
        # stack solution
        stack = []

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                pass
            else:
                stack.append("a")
        return len(stack)
    
class Solution:
    def Operations(self, logs):
        # int var solution
        steps_away_from_main = 0

        for operation in logs:
            if operation == "./" or (operation == "../" and steps_away_from_main == 0):
                pass
            elif operation == "../":
                steps_away_from_main -= 1
            else:
                steps_away_from_main += 1
        return steps_away_from_main
    
