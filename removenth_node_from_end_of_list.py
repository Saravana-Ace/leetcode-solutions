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
    
# solution 2 - using two pointer method
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next