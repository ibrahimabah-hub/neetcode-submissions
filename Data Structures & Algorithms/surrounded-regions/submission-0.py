class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()
        seen = set()
        regions = []
        lrow = len(board)
        lcol = len(board[0])

        def dfs(y,x):

            if (y,x) in seen:
                return
            seen.add((y,x))
            ds = [(0,1), (0,-1), (1,0), (-1, 0)]

            for row,col in ds:
                r, c = y+row, x+col
                if c in range(lcol) and r in range(lrow) and board[r][c]=="O" and (r,c) not in seen:
                    if (c,) not in safe:
                        safe.add((r,c))
                    dfs(r,c)

        for y in range(lrow):
            for x in range(lcol):
                if (y==0 or y==lrow-1 or x==0 or x==lcol-1) and board[y][x]=="O" and (y,x) not in seen:
                    safe.add((y,x))
                    dfs(y,x)

        for y in range(lrow):
            for x in range(lcol):
                if (y,x) not in safe:
                    board[y][x] = "X"
