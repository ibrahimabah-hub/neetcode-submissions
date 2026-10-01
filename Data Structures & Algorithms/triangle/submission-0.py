class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0]*len(triangle[-1])
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                
                dp[j] = triangle[i][j]+min(dp[j], dp[j+1])
                
            #print(dp)
        return dp[0]
