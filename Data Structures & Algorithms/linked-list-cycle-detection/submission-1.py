# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0

        cur = head
        val = 1001
        while cur:
            if not cur.next:
                break
            cur.val = val
            if cur.next.val>1000:
                return True
            cur = cur.next
        return False