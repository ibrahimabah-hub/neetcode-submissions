class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        counted = set()
        max_area = 0
        def bfs(y, x):
            q = collections.deque()
            counted.add((y,x))
            q.append([y,x])
            area = 0
            while q:
                row, col = q.popleft()
                ds = [[1,0], [-1,0], [0,1], [0,-1]]
                area +=1
                for d in ds:
                    r, c = row+d[0], col+d[1]
                    if r in range(lr) and c in range(lc) and grid[r][c]==1 and (r,c) not in counted:
                        q.append([r,c])
                        counted.add((r,c))

            return area

        for y in range(lr):
            for x in range(lc):
                if grid[y][x]==1 and (y,x) not in counted:
                    max_area = max(max_area, bfs(y,x))

        return max_area