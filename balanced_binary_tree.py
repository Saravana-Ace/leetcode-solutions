# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr_node, cnt):
            if not curr_node:
                return cnt
            
            l = dfs(curr_node.left, cnt+1)
            r = dfs(curr_node.right, cnt+1)

            if abs(l-r) <= 1:
                return max(l,r)
            else:
                return -1

        return True if dfs(root, 0) != -1 else False