// You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

// In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

// Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

// Each answer[i] is calculated considering the initial state of the boxes.
#include <vector>
#include <string>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> res = {};
        vector<int> ones = {};
        for (int i=0;boxes[i];i++) {
            if (boxes[i] == '1') {
            ones.push_back(i);
            }
        }

        for (int i=0;boxes[i];i++) {
            int temp = 0;
            for (int j = 0;j < ones.size();j++) {
            temp += abs(i - ones[j]);
            }
            res.push_back(temp);
        }
        return res;
    }
};