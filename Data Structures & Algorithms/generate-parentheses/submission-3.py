class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        seen = set()
        def dfs(i,string):
            if i>=n:
                if string not in res:
                    res.append(string)
                return
            elif string in seen:
                return
            else:
                seen.add(string)
            candidates = {}
            closed = []
            q = []
            dfs(i+1, "("+ string +")")
            dfs(i+1, string+"()")
            for x in range(len(string)-1):
                dfs(i+1, string[0:x]+"()"+string[x:])
                if string[x]=="(":
                    q.append(x)
                else:
                    start = q.pop()
                    closed.append(start)
                for start in closed:
                    dfs(i+1, string[0:start]+"("+string[start:x+1]+")"+string[x+1:])


        dfs(0, "")
        return res
