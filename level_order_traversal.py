from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp, res = [], []
        if root:
            temp.append(root.val)
        else:
            return root
        
        queue = deque()
        queue.append(root)

        while queue:
            res.append(temp)
            temp = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()

                if curr_node:
                    if curr_node.left:
                        queue.append(curr_node.left)
                        temp.append(curr_node.left.val)
                    if curr_node.right:
                        queue.append(curr_node.right)
                        temp.append(curr_node.right.val)
        return res