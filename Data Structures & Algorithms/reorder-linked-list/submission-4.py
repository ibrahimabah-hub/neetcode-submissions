# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        while head.next and prev.next:
            
            lt = head.next
            rt = prev.next
            head.next = prev
            prev.next = lt
            print(f"{head.val} -> {head.next.val}")
            head = lt
            prev = rt

        

            