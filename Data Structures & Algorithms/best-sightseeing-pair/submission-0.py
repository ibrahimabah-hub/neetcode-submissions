class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        dp = [float("-inf")]*(len(values)+1)
        cur_max = 0
        for i in range(len(values)-1, -1, -1):
            dp[i] = max(values[i]-i, dp[i+1])
            cur_max = max(cur_max, dp[i+1]+values[i]+i)
        #print(dp)
        return cur_max