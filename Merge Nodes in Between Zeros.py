from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        stack = []

        res = ret = ListNode()
        while start != None:
            temp = 0
            stack.append(start.val)

            if start.val == 0:
                while stack:
                    temp += stack.pop()
                new_node = ListNode(temp)
                ret.next = new_node
                ret = ret.next

            start = start.next
        
        return res.next.next
