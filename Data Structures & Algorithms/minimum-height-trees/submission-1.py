class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n ==1:
            return [0]
        if n==2:
            return [0,1]
        es = {}

        for a,b in edges:
            es[a] = es.get(a, [])
            es[a].append(b)
            es[b] = es.get(b, [])
            es[b].append(a)

        res = []
        low = float("inf")

        for i in range(n):
            level = 1
            q = collections.deque()
            cur = set()
            cur.add(i)
            for edge in es[i]:
                q.append((edge, 1))
            while(q):
                node, l = q.popleft()
                if node in cur:
                    continue
                cur.add(node)
                level = max(level, l)
                for edge in es[node]:
                    if edge not in cur:
                        q.append((edge, l+1))

            if level<low:
                low = level
                res.clear()
                res.append(i)
            elif level==low:
                res.append(i)

        return res
                