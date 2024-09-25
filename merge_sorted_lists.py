# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        else:
            curr_l1 = list1
            curr_l2 = list2

            while curr_l1 and curr_l2:
                if curr_l1.val == curr_l2.val:
                    temp_node = ListNode(curr_l1.val)
                    hold_next = curr_l1.next
                    curr_l1.next = temp_node
                    temp_node.next = hold_next
                    curr_l1 = hold_next
                    curr_l2 = curr_l2.next
                elif curr_l2.val >= curr_l1.val:
                    curr_l1 = curr_l1.next
                else:
                    temp_val = curr_l1.val
                    curr_l1.val = curr_l2.val
                    hold_next = curr_l1.next

                    new_node = ListNode(temp_val)
                    new_node.next = hold_next
                    curr_l1.next = new_node
                    curr_l2 = curr_l2.next

            check = list1
            if not curr_l1 and curr_l2:
                while True:
                    if not check:
                        break
                    if check.next == None:
                        check.next = curr_l2
                        break
                    check = check.next
            
            return list1