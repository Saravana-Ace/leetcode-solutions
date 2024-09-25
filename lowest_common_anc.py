# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        #check case in which in left and right
        def dfs(curr_node):
            nonlocal res

            if not curr_node:
                return False

            l = dfs(curr_node.left)
            r = dfs(curr_node.right)

            if l and r:
                res = curr_node
            elif curr_node.val == p.val or curr_node.val == q.val:
                if l or r:
                    res = curr_node
                return True
            
            return l or r
        
        dfs(root)
        return res