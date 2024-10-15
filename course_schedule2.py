#can also use kahn's algo, detecting a loop using bfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_mapper = {i:[] for i in range(numCourses)}
        
        for a, b in prerequisites:
            adj_mapper[a].append(b)

        cur_rec_visited = set()
        overall_visited = set()
        
        def dfs(course):
            if course in cur_rec_visited:
                return False
            # if course in overall_visited:
            #     return True
            if not adj_mapper[course]:
                return True
            
            # overall_visited.add(course)
            cur_rec_visited.add(course)
            for neighbor in adj_mapper[course]:
                if not dfs(neighbor): return False
            cur_rec_visited.remove(course)
            adj_mapper[course] = []

            return True
        
        for course in range(numCourses-1):
            if not dfs(course): return False
        
        return True