class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i = 0
        res = curr_inc = curr_dec = 1

        while i+1 < len(nums):
            if nums[i] < nums[i+1]:
                curr_inc += 1
                curr_dec = 1
            elif nums[i] > nums[i+1]:
                curr_dec += 1
                curr_inc = 1
            else:
                curr_dec = curr_inc = 1
            res = max(res, curr_inc, curr_dec)
            i += 1
        
        return res