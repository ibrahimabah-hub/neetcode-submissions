"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        nodes = {}
        root = None
        q = collections.deque()
        q.append(node)

        cloned = {}
        done = set()
        while(q):
            cur = q.popleft()
            if cur.val not in cloned:
                cloned[cur.val] = Node(cur.val)
                
            clone = cloned[cur.val]
            if cur.val in done:
                continue

            for neighbor in cur.neighbors:
                if neighbor.val not in cloned:
                    cloned[neighbor.val] = Node(neighbor.val)
                clone.neighbors.append(cloned[neighbor.val])
                if neighbor.val in done:
                    continue
                q.append(neighbor)

            done.add(cur.val)

        return cloned[node.val]
            
