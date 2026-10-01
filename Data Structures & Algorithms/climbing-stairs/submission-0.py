class Solution:
    def climbStairs(self, n: int) -> int:
        types = {}
        
        for i in range(n):
            if i+1 <=n:
                types[i+1] = types.get(i,1)+types.get(i+1, 0)
            if i+2 <=n:
                types[i+2] = types.get(i,1)+types.get(i+2, 0)

        return types[n]