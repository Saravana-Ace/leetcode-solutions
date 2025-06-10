class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(temp, nums):
            res.append(temp[:])
            if not nums:
                return
            
            for i in range(len(nums)):
                temp.append(nums[i])
                backtrack(temp, nums[i+1:len(nums)])
                temp.pop()
        
        backtrack([], nums)
        
        return res