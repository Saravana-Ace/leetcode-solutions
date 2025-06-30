import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        k = len(nums)-k+1
        temp = []
        res = -1
        
        for num in nums:
            heapq.heappush(temp, int(num))

        for i in range(k):
            res = heapq.heappop(temp)
        
        return str(res)