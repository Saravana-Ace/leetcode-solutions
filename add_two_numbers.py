# solution 1 - iterative
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        prev = ListNode()
        while temp != None:
            hold = temp.next
            temp.next = prev
            prev = temp
            temp = hold
        
        start1 = prev
        temp = l2
        prev = ListNode()
        while temp != None:
            hold = temp.next
            temp.next = prev
            prev = temp
            temp = hold
        
        start2 = prev
        first = []
        while start1.next != None:
            first.append(f"{start1.val}")
            start1 = start1.next

        second = []
        while start2.next != None:
            second.append(f"{start2.val}")
            start2 = start2.next
        
        a = int("".join(first))
        b = int("".join(second))

        c = a + b
        c = str(c)
        res = ListNode()
        temp = res
        for i in range(len(c)-1, -1, -1):
            temp.val = int(c[i])
            if i == 0: break
            temp.next = ListNode()
            temp = temp.next

        return res