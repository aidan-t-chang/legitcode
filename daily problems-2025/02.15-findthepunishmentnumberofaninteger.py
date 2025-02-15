# Given a positive integer n, return the punishment number of n.

# The punishment number of n is defined as the sum of the squares of all integers i such that:

# 1 <= i <= n
# The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer 
# values of these substrings equals i.

class Solution:
    def find_partitions(
        self, start_index, current_sum, string_num, target, memo
    ):
        if start_index == len(string_num):
            return current_sum == target

        if current_sum > target:
            return False

        if memo[start_index][current_sum] != -1:
            return memo[start_index][current_sum] == 1

        partition_found = False

        for current_index in range(start_index, len(string_num)):
            current_string = string_num[start_index : current_index + 1]
            addend = int(current_string)
            partition_found = partition_found or self.find_partitions(
                current_index + 1,
                current_sum + addend,
                string_num,
                target,
                memo,
            )
            if partition_found:
                memo[start_index][current_sum] = 1
                return True
        memo[start_index][current_sum] = 0
        return False

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0
        for current_num in range(1, n + 1):
            square_num = current_num * current_num
            string_num = str(square_num)
            memo_array = [
                [-1] * (current_num + 1) for _ in range(len(string_num))
            ]
            if self.find_partitions(0, 0, string_num, current_num, memo_array):
                punishment_num += square_num

        return punishment_num