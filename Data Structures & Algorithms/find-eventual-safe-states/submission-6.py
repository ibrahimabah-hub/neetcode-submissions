import collections
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = set()
        edges = {}
        q = collections.deque()
        for i in range(len(graph)):
            for v in graph[i]:
                edges[v] = edges.get(v, [])
                edges[v].append(i)
            if len(graph[i])<1:
                q.append(i)

        while(q):
            cur = q.popleft()
            if cur in res:
                continue
            if len(graph[cur])<1:
                res.add(cur)
            else:
                res.add(cur)
                for v in graph[cur]:
                    if (v not in res or v==cur ) and cur in res:
                        res.remove(cur)
            if cur in res and cur in edges:
                for e in edges[cur]:
                    if e not in res:
                        q.append(e)

        return list(res)
