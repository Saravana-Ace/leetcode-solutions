from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_mapper = {i:[] for i in range(numCourses)}
        
        for a, b in prerequisites:
            adj_mapper[a].append(b)

        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if not adj_mapper[course]:
                return True
            
            visited.add(course)
            for neighbor in adj_mapper[course]:
                if not dfs(neighbor): return False
            visited.remove(course)
            adj_mapper[course] = []

            return True
        
        for course in range(numCourses-1):
            if not dfs(course): return False
        
        return True