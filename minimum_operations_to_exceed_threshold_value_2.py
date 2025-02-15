import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0

        # since its a heap the first and second values are 
        # in order so no need to min or max
        while nums[0] < k:
            op = heapq.heappop(nums) * 2 + heapq.heappop(nums)
            heapq.heappush(nums, op)
            res += 1

        return res