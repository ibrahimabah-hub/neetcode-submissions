import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        hq.heapify(heap)
        while len(heap)>k:
            hq.heappop(heap)

        return(heap[0])