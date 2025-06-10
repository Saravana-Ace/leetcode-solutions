class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def backtrack(temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            for num in nums:
                if num in visited: continue
                temp.append(num)
                visited.add(num)
                backtrack(temp)
                visited.remove(temp.pop())

        
        backtrack([])
        return res