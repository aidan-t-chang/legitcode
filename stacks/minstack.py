# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minvalues = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minvalues[-1] if self.minvalues else val)
        self.minvalues.append(val)
    def pop(self):
        self.stack.pop()
        self.minvalues.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minvalues[-1]