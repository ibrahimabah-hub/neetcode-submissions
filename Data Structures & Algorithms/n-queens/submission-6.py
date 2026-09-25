class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = []
        def checkColumn(x):
            for i in range(n):
                if [i, x] in board:
                    return False
            return True
        
        def checkRow(y):
            for i in range(n):
                if [y, i] in board:
                    return False
            return True

        def checkDiagonal(y, x):
            x1 = x
            y1 = y
            while(y1>=0 and x1>=0):
                for i in range(len(ys)):
                    if ys[i]==y1 and xs[i]==x1:
                        return False
                y1-=1
                x1-=1

            x1 = x
            y1 = y
            while(y1<n and x1<n):
                for i in range(len(ys)):
                    if ys[i]==y1 and xs[i]==x1:
                        return False
                x1+=1
                y1+=1
            
            x1 = x
            y1 = y
            while(y1>=0 and x1<n):
                for i in range(len(ys)):
                    if ys[i]==y1 and xs[i]==x1:
                        return False
                x1+=1
                y1-=1

            x1 = x
            y1 = y
            while(y1<n and x1>=0):
                for i in range(len(ys)):
                    if ys[i]==y1 and xs[i]==x1:
                        return False
                x1-=1
                y1+=1

            return True
        ys = set()
        xs = set()
        pd = set()
        nd = set()
        board = [["."] * n for x in range(n)]
        def dfs(y1):
            if y1>=n:
                copy = ["".join(row) for row in board]
                if copy not in res:
                    
                    res.append(copy)
                return
            
            for x1 in range(n):
                if x1 in xs:
                    continue
                if y1+x1 in pd:
                    continue
                if y1-x1 in nd:
                    continue
                xs.add(x1)
                pd.add(y1+x1)
                nd.add(y1-x1)
                board[y1][x1] = "Q"
                dfs(y1+1)
                board[y1][x1] = "."
                xs.remove(x1)
                pd.remove(y1+x1)
                nd.remove(y1-x1)

        dfs(0)

        return res
                    

                    