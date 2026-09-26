class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        island = []
        counted = set()

        def bfs(y,x):
            q = collections.deque()
            counted.add((y,x))
            q.append((y,x))
            ds = [[0, 1], [0,-1], [1, 0], [-1, 0]]
            while q:
                row, col = q.popleft()
                counted.add((row, col))
                for d in ds:
                    r, c = row+d[0], col+d[1]
                    if r in range(len(grid)) and c in range(len(grid[r])) and grid[r][c]=="1"  and (r,c) not in counted:
                        q.append([r,c])
                        counted.add((r,c))


        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x]=="1" and (y,x) not in counted:
                    bfs(y,x)
                    islands+=1

        return islands