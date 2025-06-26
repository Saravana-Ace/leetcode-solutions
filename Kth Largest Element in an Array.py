import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []
        for num in nums:
            heapq.heappush(temp, -num)
        
        res = -1
        for i in range(k):
            res = heapq.heappop(temp)

        return -res
