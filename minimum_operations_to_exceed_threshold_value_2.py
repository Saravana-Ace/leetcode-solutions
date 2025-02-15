import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        
        while nums[0] < k:
            op = heapq.heappop(nums) * 2 + heapq.heappop(nums)
            heapq.heappush(nums, op)
            res += 1

        return res