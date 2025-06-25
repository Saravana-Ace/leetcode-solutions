class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        start_range = 0
        end_range = 0

        for i in range(len(nums)):
            if nums[i] == key:
                start_range = max(end_range, i-k)
                end_range = min(i+k+1, len(nums))

                for val in range(start_range, end_range):
                    res.append(val)
        return res
