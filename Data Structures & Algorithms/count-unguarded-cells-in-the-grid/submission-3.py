class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        gs = set()
        ws = set()
        seen = set()
        safe = m * n
        for g in guards:
            seen.add((g[0], g[1]))
            gs.add((g[0], g[1]))
        for w in walls:
            seen.add((w[0], w[1]))
            ws.add((w[0], w[1]))
        for y,x in guards:
            curx = x+1
            while(curx<n and (y,curx) not in gs and (y,curx) not in ws):
                if (y, curx) not in seen:
                    #print(f"blocking {y, curx}")
                    seen.add((y, curx))
                curx+=1
            curx = x-1
            while(curx>=0 and (y,curx) not in gs and (y,curx) not in ws):
                if (y, curx) not in seen:
                    #print(f"blocking {y, curx}")
                    seen.add((y, curx))
                curx-=1
            cury = y+1
            while(cury<m and (cury,x) not in gs and (cury,x) not in ws):
                if (cury, x) not in seen:
                    #print(f"blocking {cury, x}")
                    seen.add((cury, x))
                cury+=1
            cury = y-1
            while(cury>=0 and (cury,x) not in gs and (cury,x) not in ws):
                if (cury, x) not in seen:
                    #print(f"blocking {cury, x}")
                    seen.add((cury, x))
                cury-=1

        return (m*n)-len(seen)

                    