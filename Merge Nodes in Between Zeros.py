# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = res = ListNode()
        start = head
        temp = 0
        
        while start:
            temp += start.val
            if start.val == 0:
                new_node = ListNode(temp)
                res.next = new_node
                res = res.next
                temp = 0

            start = start.next
        return ret.next.next
