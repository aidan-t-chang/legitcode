# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        pre = {i:[] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            pre[crs].append(prereq)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if pre[crs] == []:
                return True
            
            visit.add(crs)
            for prereq in pre[crs]:
                if not dfs(prereq):
                    return False
            
            visit.remove(crs)
            pre[crs] = [] 
            # if dfs on this course ever needs to be run again, setting it to empty list will prevent repetitive calls
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True