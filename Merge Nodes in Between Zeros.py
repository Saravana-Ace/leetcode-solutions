# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = res = ListNode()
        start = head
        temp, count, prev = 0, 0 , None
        
        while start:
            temp += start.val

            if start.val == 0:
                start.val = temp
                temp = 0
                res.next = start
                res = res.next
            
            start = start.next
        
        return ret.next.next
