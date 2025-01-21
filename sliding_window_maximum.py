from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            if queue and i - queue[0] + 1 > k:
                queue.popleft()

            queue.append(i)

            if queue and i+1 == k or i+1 > k:
                res.append(nums[queue[0]])
        
        return res