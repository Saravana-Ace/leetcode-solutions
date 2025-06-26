# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        start = head
        temp, count, prev = 0, 0 , None
        
        while start:
            temp += start.val

            if start.val == 0:
                if count == 1:
                    res = start
                elif count > 1:
                    prev.next = start
                
                start.val = temp
                temp = 0
                count += 1
                prev = start
            start = start.next
        
        return res
