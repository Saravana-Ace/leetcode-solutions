# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lower_li = ListNode()
        higher_li = ListNode()
        curr_node = head
        res = lower_li
        temp = higher_li

        while curr_node:
            if curr_node.val < x:
                lower_li.next = curr_node
                lower_li = lower_li.next
            else:
                higher_li.next = curr_node
                higher_li = higher_li.next
            
            curr_node = curr_node.next
        
        lower_li.next = temp.next
        higher_li.next = None
        return res.next