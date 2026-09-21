# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lnum = l1.val
        rnum = l2.val

        l1 = l1.next
        l2 = l2.next
        place = 1
        while l1:
            prod = 1
            for i in range(place):
                prod *= 10
            cur = l1.val*prod
            lnum += cur
            l1 = l1.next
            place+=1

        place = 1
        while l2:
            prod = 1
            for i in range(place):
                prod *= 10
            cur = l2.val*prod
            rnum += cur
            l2 = l2.next
            place+=1

        add = lnum + rnum
        print(add)
        val = add%10
        l3 = ListNode(val)
        cur = l3
        while add>=10:
            add=add//10
            val = add%10
            print(val)
            cur.next = ListNode(val)
            cur = cur.next
        
        return l3
        

