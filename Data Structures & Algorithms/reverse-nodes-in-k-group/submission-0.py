# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        nhead = head
        tail = head
        khead = head
        pre = None
        times = 0
        while cur:
            times +=1
            #print(f"idx: {times}, cur: {cur.val}")
            if times%k==0:
                #print(f"reversing at idx: {times}")
                if times == k:
                    nhead = cur
                #print(f"{cur.val}->{cur.next.val}")
                tmp = cur.next
                cur.next = None
                section = self.reverse(tmp, khead)
                #print(f"new start: {section.val}->")
                if pre:
                    pre.next = section
                pre = khead
                khead = tmp
                cur = tmp
                continue
            cur = cur.next
            
        
        return nhead


    def reverse(self, prev: Optional[ListNode], cur: ListNode) -> Optional[ListNode]:
        #print("rev")
        while(cur):
            tmp = cur.next
            cur.next = prev
            prev = cur
           
            if tmp:
                cur = tmp
            else:
                break
        return cur

            
