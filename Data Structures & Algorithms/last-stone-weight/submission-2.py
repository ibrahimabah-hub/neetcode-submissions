class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while(len(stones)>1):
            cur = heapq.heappop_max(stones)
            cur2 = heapq.heappop_max(stones)
            if cur>cur2:
                heapq.heappush_max(stones, cur-cur2)

        if stones:
            return stones[0]
        return 0
