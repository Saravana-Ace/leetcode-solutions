# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = root
        def dfs(curr_node):
            if curr_node == None:
                return
            
            temp = curr_node.left
            curr_node.left = curr_node.right
            curr_node.right = temp
            
            dfs(curr_node.left)
            dfs(curr_node.right)
            
        dfs(root)
        return res