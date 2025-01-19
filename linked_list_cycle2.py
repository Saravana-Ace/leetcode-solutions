# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False

# solution 2 - changing values until you see the same one
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head != None:
            if head.val == float('inf'): return 1
            head.val = float('inf')
            head = head.next
        return 0