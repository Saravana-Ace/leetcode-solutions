import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]

        heapq.heapify(nums)
        res = -1
        k = len(nums)-k+1
        for i in range(k):
            res = heapq.heappop(nums)
        
        return str(res)