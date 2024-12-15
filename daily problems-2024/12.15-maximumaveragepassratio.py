import heapq

# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, 
# where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, 
# but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students 
# that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents 
# students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. 
# The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        def calculate_gain(pas, total):
            return (pas + 1) / (total + 1) - pas / total
        
        heap = []
        for passes, students in classes:
            gain = calculate_gain(passes, students)
            heapq.heappush(heap, (-1 * gain, passes, students))

        for i in range(extraStudents):
            g, p, t = heapq.heappop(heap)

            heapq.heappush(heap, (-1 * (calculate_gain(p+1, t+1)), p+1, t+1))

        res = 0
        while heap:
            gain, pas, tot = heapq.heappop(heap)
            res += pas / tot
        return res / len(classes)