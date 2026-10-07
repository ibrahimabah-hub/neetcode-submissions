class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()
        seen = set()
        out = []
        lcol = len(heights[0])
        lrow = len(heights)

        def dfs(y,x):

            seen.add((y,x))
            ds = [(0,1), (0,-1), (1,0), (-1,0)]

            if y==0 or x==0:
                pac.add((y,x))
            if y==lrow-1 or x==lcol-1:
                atl.add((y,x))

            for d in ds:
                r, c  = y+d[0], x+d[1]

                if c in range(lcol) and r in range(lrow) and heights[r][c]<=heights[y][x]:
                    if (r,c) not in seen:
                        dfs(r,c)
                    if (r, c) in atl:
                        atl.add((y,x))
                    if (r, c) in pac:
                        pac.add((y,x))

            if (y,x) in atl and (y,x) in pac:
                out.append((y,x))

                    
        for y in range(lrow):
            for x in range(lcol):
                if (y,x) not in seen:
                    dfs(y,x)

        print(atl)
        print(pac)

        return out