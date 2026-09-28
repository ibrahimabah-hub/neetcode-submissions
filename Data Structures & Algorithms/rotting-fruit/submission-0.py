class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        lr = len(grid)
        lc = len(grid[0])
        q = collections.deque()
        seen = set()
        app = 0
        for row in range(lr):
            for col in range(lc):
                if grid[row][col] ==2:
                    q.append([row, col, 0])
                if grid[row][col]==1:
                    app+=1
        maxtime = 0
        while(q):
            if app==0:
                break
            rot = q.popleft()
            row, col, t1 = rot[0], rot[1], rot[2]
            
            if (row,col) in seen:
                continue
            seen.add((row,col))
            ds = ([0,1], [0,-1], [1,0], [-1,0])
            for d in ds:
                r,c = row+d[0], col+d[1]
                #print(f"r, c = {r, c}")
                if r in range(lr) and c in range(lc) and grid[r][c]==1:
                    #print(f"apple rotted at{r},{c}")
                    grid[r][c]=2
                    app-=1
                    q.append([r,c,t1+1])
                    maxtime= max(t1+1, maxtime)
                    

        if app>0:
            #print(f"total apples = {app}")
            return -1

        return maxtime

        