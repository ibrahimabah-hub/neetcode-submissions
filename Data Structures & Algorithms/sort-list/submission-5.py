# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def split(head):
            slow = head
            fast = head
            cur = head
            while slow.next and fast and fast.next:
                cur = slow
                slow = slow.next
                fast = fast.next.next
            cur.next = None
            return head, slow

        def merge(head):
            if not head:
                return None
            if not head.next:
                return head
            
            l, r = split(head)
            if r.next:
                r = merge(r)
            if l.next:
                l = merge(l)
            print(l.val, r.val)
            cur = ListNode()
            root = cur
            while(l or r):
                if not l:
                    cur.next = r
                    break
                elif not r:
                    cur.next = l
                    break
                else:
                    if l.val<r.val:
                        cur.next = l
                        l = l.next
                    else:
                        cur.next = r
                        r = r.next
                    cur = cur.next
            
            return root.next

        return merge(head)