class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer moore algo
        res = nums[0]
        cnt = 1

        for i in range(1, len(nums)):
            if cnt == 0:
                res = nums[i]
            cnt += (1 if nums[i]==res else -1)
        return res