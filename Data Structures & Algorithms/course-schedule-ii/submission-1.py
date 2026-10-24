class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        need = {}
        helps = {}
        res = []
        for req in prerequisites:
            need[req[0]] = need.get(req[0], [])
            need[req[0]].append(req[1])
            helps[req[1]] = helps.get(req[1], [])
            helps[req[1]].append(req[0])
        done = set()
        q = collections.deque()
        for num in range(numCourses):
            if num not in need:
                q.append(num)

        while(q):

            cur = q.popleft()
            if cur in done:
                continue
            if cur not in need or len(need[cur])==0:
                res.append(cur)
                done.add(cur)
                if cur in helps:
                    for req in helps[cur]:
                        need[req].remove(cur)
                        q.append(req)
        
        if len(res)<numCourses:
            return []
        return res