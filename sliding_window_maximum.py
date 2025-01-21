from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        check = k-1
        
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            if queue and i - queue[0] > check:
                queue.popleft()

            queue.append(i)

            if i+1 >= k:
                res.append(nums[queue[0]])
        
        return res

# solution 2 - using neetcode sliding window
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        res = []
        queue = deque()
        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if (r+1) >= k:
                res.append(nums[queue[0]])
                l += 1
            r += 1
        
        return res