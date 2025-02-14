from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        sub = [nums[i]-i for i in range(len(nums))]
        
        mapper = Counter(sub)
        res = 0

        for c in mapper.values():
            res += (c * (c-1))
        
        return (len(sub) * (len(sub)-1) - res)//2