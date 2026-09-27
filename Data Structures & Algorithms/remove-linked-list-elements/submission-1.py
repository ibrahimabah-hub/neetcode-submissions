# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        cur = ListNode()
        root = cur
        cur.next = head
        while(cur):
            while cur.next and cur.next.val==val:
                cur.next = cur.next.next
            cur = cur.next

        return root.next