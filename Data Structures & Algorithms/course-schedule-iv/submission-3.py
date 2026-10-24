class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        need = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for a,b in prerequisites:
            #print(a,b)
            need[a][b] = 1
            #print(need)

        def dfs(a,b):
            for i in range(numCourses):
                if need[b][i]==1 and need[a][i]==0:
                    need[a][i]=1
                    dfs(a,i)

        for a,b in prerequisites:
            dfs(a,b)
        #print(need)
        res = []
        for q in queries:
            if need[q[0]][q[1]]==1:
                res.append(True)
            else:
                res.append(False)
        return res