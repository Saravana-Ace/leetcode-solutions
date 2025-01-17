# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        vals = []
        while temp != None:
            vals.append(temp.val)
            temp = temp.next
        
        i = len(vals)-1
        temp = head
        while i >= 0:
            temp.val = vals[i]
            i -= 1
            temp = temp.next
        
        return head
    
# solution 2 - flipping the direction of the pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = end
            end = curr
            curr = temp

        return end