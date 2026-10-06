class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        tots = {}
        for num in hand:
            tots[num] = 1+tots.get(num, 0)
        heap = list(tots.keys())
        heapq.heapify(heap)
        while heap:
            cur = heap[0]
            for i in range(cur, cur+groupSize):
                if i not in tots:
                    #print(f"{cur+i} not in heap")
                    return False
                tots[i]-=1
                if tots[i] ==0:
                    if i!=heap[0]:
                        return False
                    heapq.heappop(heap)
        
        return True
                
