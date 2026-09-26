class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        lr = len(grid)
        lc = len(grid[0])
        visit = set()
        q = collections.deque()
        dist = 0
        def addRoom(r, c, q, d):
            if r in range(lr) and c in range(lc) and (r,c) not in visit and grid[r][c]>d:
                grid[r][c] = d
                visit.add((r,c))
                q.append((r,c,d))
                
        for y in range(lr):
            for x in range(lc):
                if grid[y][x] == 0:
                    q.append((y,x,0))
                    visit.add((y,x))
        
        while q:
            r,c,d = q.popleft()
            addRoom(r,c+1, q, d+1)
            addRoom(r,c-1, q, d+1)
            addRoom(r+1,c, q, d+1)
            addRoom(r-1,c, q,d+1)
            
