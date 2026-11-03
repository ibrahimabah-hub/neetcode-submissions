class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[False for _ in range(n)] for _ in range(n)]

        for a,b in edges:
            adj_list[a][b] = True
            adj_list[b][a] = True

        seen = set()

        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for j in range(n):
                if adj_list[i][j]==True and j not in seen:
                    dfs(j)
        comp = 0
        for i in range(n):
            if i not in seen:
                comp+=1
                dfs(i)
        

        return(comp)