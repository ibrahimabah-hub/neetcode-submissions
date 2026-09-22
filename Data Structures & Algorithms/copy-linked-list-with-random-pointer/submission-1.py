"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_copied = {}
        if not head:
            return None
        cur = head
        copy_head = None
        while cur:
            copy = Node(cur.val)
            if not copy_head:
                copy_head = copy
            nodes_copied[cur] = copy
            if cur.random:
                if cur.random not in nodes_copied:
                    pass
                else:
                    copy.random = nodes_copied[cur.random]
            if cur.next:
                if cur.next not in nodes_copied:
                    pass
                else:
                    copy.next = nodes_copied[cur.next]

            cur = cur.next

        cur = head
        while cur:
            copy = nodes_copied[cur]
            if cur.random:
                copy.random = nodes_copied[cur.random]
            if cur.next:
                copy.next = nodes_copied[cur.next]
            cur = cur.next

        return copy_head