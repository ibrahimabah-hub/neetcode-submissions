import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = stones
        hq.heapify_max(minheap)

        while len(minheap)>1:
            x = hq.heappop_max(minheap)
            y = hq.heappop_max(minheap)
            print(x, y)
            print(minheap)
            if x>y:
                hq.heappush_max(minheap, x-y)
        
        return minheap[0] if minheap else 0

