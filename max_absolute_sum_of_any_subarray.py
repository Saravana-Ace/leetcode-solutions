class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = res1 = res2 = 0
        for num in nums:
            res1 = num if res1 < 0 else res1 + num
            res2 = num if res2 > 0 else res2 + num
            
            res = max(res, res1, -res2)

        return res