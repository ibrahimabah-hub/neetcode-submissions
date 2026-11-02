# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head.next
        while l and r:
            cur = 0
            ldiv = set()
            for i in range(1, int(math.pow(l.val, .5))+1):
                inv = l.val//i
                if inv!=l.val/i:
                    continue
                ldiv.add(i)
                ldiv.add(inv)
            for num in ldiv:
                if r.val//num==r.val/num and num>cur:
                    cur = num
            node = ListNode(cur, r)
            l.next = node
            l = r
            r = l.next

        return head

