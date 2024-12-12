# Design a stack that supports increment operations on its elements.

# Implement the CustomStack class:

# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
# void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
# int pop() Pops and returns the top of the stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max:
            self.stack.append(x)

    def pop(self) -> int:
        n = self.stack.pop() if self.stack else -1
        return n

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack)) # no matter what, k will always be at most all the elements in the stack
        for _ in range(k):
            self.stack[_] += val
    

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)