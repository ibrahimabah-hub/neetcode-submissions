class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        need = {}
        helps = {}

        for a,b in prerequisites:
            need[a] = need.get(a, [])
            need[a].append(b)
            helps[b] = helps.get(b, [])
            helps[b].append(a)

        q = collections.deque()
        done = set()

        for i in range(numCourses):
            if i not in need:
                q.append(i)
        

        while(q):
            cur = q.popleft()
            if cur in done:
                continue
            if cur not in need or len(need[cur])<1:
                done.add(cur)
                if cur in helps:
                    for i in helps[cur]:
                        if cur in need[i]:
                            need[i].remove(cur)
                        q.append(i)

        if len(done)==numCourses:
            return True
        return False