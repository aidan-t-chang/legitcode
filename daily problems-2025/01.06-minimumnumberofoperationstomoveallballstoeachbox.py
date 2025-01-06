# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.


class Solution:
    def minOperations(self, boxes: str):
        count = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                count.append(i)

        res = []

        for i in range(len(boxes)):
            temp = 0
            for c in count:
                temp += abs(c - i)
            res.append(temp)

        return res