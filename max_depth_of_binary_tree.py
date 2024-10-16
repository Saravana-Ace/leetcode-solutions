from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root: return 0
        
        # queue = deque()
        # queue.append(root)
        # res = 0

        # while queue:
        #     for _ in range(len(queue)):
        #         curr = queue.popleft()
        #         if curr.left: queue.append(curr.left)
        #         if curr.right: queue.append(curr.right)
        #     res += 1
        
        # return res

        def dfs(curr):
            if not curr:
                return 0
            
            return max(dfs(curr.left)+1, dfs(curr.right)+1)

        return dfs(root)