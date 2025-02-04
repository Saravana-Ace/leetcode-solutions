class Solution:
    def check(self, nums: List[int]) -> bool:
        count = i = 0
        while i + 1 < len(nums):
            if nums[i] > nums[i+1]:
                count += 1
            if count > 1:
                return False
            i += 1

        if count == 1 and nums[-1] > nums[0]:
            return False
        
        return True