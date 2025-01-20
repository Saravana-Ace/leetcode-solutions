# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        ret = res

        while list1 and list2:
            if list2.val >= list1.val:
                res.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            
            res = res.next
        
        if list1 and not list2:
            res.next = list1
        elif list2 and not list1:
            res.next = list2

        return ret.next

# solution 3 - similar to solution 2 but everything is inside the loop
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = temp = ListNode()
        
        while True:
            if not list1:
                temp.next = list2
                break
            elif not list2:
                temp.next = list1
                break
            
            if list1.val >= list2.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            
            temp = temp.next
        
        return res.next