class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        
        for i in range(len(nums)):
            d = target-nums[i]
            if d in mapper:
                return [i, mapper[d]]
            else:
                mapper[nums[i]] = i