class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()

        def dfs(i):
            if (i) in seen:
                return
            seen.add(i)

            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and j not in seen:
                    dfs(j)

        prov = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1 and j not in seen:
                    print(f"{j} not seen")
                    prov+=1
                    dfs(j)

        return prov