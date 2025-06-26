# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = res = ListNode()
        start = head
        slow = head
        while start:
            temp = 0
            if start.val == 0:
                while slow != start:
                    temp += slow.val
                    slow = slow.next
                new_node = ListNode(temp)
                res.next = new_node
                res = res.next
            start = start.next
        
        return ret.next.next
