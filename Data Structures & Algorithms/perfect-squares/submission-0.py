class Solution:
    def numSquares(self, n: int) -> int:
        cur = [0]
        perf = 1
        while cur[-1]<=n:
            cur.append(perf*perf)
            perf+=1
        cur.pop()
        dp = [float("inf")]*(n+1)
        for num in cur:
            dp[num] = 1
        for i in range(n+1):
            for num in cur:
                if i>=num:
                    dp[i] = min(dp[i], dp[num]+dp[i-num])

        return dp[n]

