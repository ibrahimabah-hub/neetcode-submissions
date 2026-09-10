class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices)==0:
            return 0
        buy = prices[0]
        sell = 0
        for i in range(len(prices)):
            if prices[i]< buy:
                buy = prices[i]
            cur =  prices[i] - buy
            profit = max(cur, profit)

        return(profit)