from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        queue = deque()
        queue.append(node)
        
        mapper = {}

        if node:
            mapper[1] = Node(1, None)
            while queue:
                for _ in range(len(queue)):
                    curr_node = queue.popleft()
                    
                    for neighbor in curr_node.neighbors:
                        if neighbor.val in mapper:
                            mapper[curr_node.val].neighbors.append(mapper[neighbor.val])
                        else:
                            temp = Node(neighbor.val, None)
                            mapper[curr_node.val].neighbors.append(temp)
                            mapper[neighbor.val] = temp
                            queue.append(neighbor)
        
            return mapper[1]
        return node