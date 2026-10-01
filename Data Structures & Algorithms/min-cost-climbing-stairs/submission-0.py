class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = {}
        
        for i in range(len(cost)):
            minCost[i] = min(minCost.get(i-1, 0), minCost.get(i-2, 0))+cost[i]


        return min(minCost[len(cost)-1], minCost[len(minCost)-2])