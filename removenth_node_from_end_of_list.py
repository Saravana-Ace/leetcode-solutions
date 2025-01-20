# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 1
        while temp != None:
            length += 1
            temp = temp.next
        
        res = ListNode()
        res.next = head
        temp = res

        i = 0
        while i != length-n-1:
            i += 1
            temp = temp.next
        
        temp.next = temp.next.next

        return res.next