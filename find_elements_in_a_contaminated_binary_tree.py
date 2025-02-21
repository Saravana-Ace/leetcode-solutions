from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        queue = deque([root])
        root.val = 0
        self.exists = set()

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                self.exists.add(curr.val)
                
                if curr.left:
                    curr.left.val = (curr.val*2) + 1
                    queue.append(curr.left)
                if curr.right:
                    curr.right.val = (curr.val*2) + 2
                    queue.append(curr.right)

        

    def find(self, target: int) -> bool:
        return True if target in self.exists else False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)