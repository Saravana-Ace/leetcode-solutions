class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = res = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            res = max(res, curr_sum)
            if i+1 < len(nums) and nums[i] >= nums[i+1]:
                curr_sum = 0
        return res