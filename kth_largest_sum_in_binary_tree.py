from collections import deque
import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            temp = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                temp += (-curr.val)

                if curr and curr.left:
                    queue.append(curr.left)
                if curr and curr.right:
                    queue.append(curr.right)
            heappush(res, temp)
        
        if k > len(res): return -1
        
        for i in range(k):
            if i == k-1:
                return -heappop(res)
            heappop(res)