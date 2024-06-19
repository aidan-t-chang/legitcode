# You have n jobs and m workers. 
# You are given three arrays: difficulty, profit, and worker where:

# difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
# worker[j] is the ability of jth worker 
# (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
# Every worker can be assigned at most one job, 
# but one job can be completed multiple times.

# For example, if three workers attempt the same job that pays $1, 
# then the total profit will be $3. If a worker cannot complete any job, 
# their profit is $0.
# Return the maximum profit we can achieve after assigning the workers to the jobs.

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        max_difficulty = max(difficulty)
        max_profit_up_to_difficulty = [0] * (max_difficulty + 1)

        for d, p in zip(difficulty, profit):
            max_profit_up_to_difficulty[d] = max(max_profit_up_to_difficulty[d], p)

        for i in range(1, max_difficulty + 1):
            max_profit_up_to_difficulty[i] = max(max_profit_up_to_difficulty[i], max_profit_up_to_difficulty[i - 1])

        total_profit = 0
        for ability in worker:
            if ability > max_difficulty:
                total_profit += max_profit_up_to_difficulty[max_difficulty]
            else:
                total_profit += max_profit_up_to_difficulty[ability]

        return total_profit