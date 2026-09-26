class MedianFinder:

    def __init__(self):
        self.sheap = []
        self.lheap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.sheap, num)
        if self.sheap and self.lheap and self.sheap[0] > self.lheap[0]:
            heapq.heappush(self.lheap, heapq.heappop_max(self.sheap))
        if len(self.sheap)-len(self.lheap)>1:
            heapq.heappush(self.lheap, heapq.heappop_max(self.sheap))
        if len(self.lheap)-len(self.sheap)>1:
            heapq.heappush_max(self.sheap, heapq.heappop(self.lheap))


    def findMedian(self) -> float:
        if len(self.sheap)>len(self.lheap):
            return self.sheap[0]
        elif len(self.lheap)>len(self.sheap):
            return self.lheap[0]
        else:
            return((self.sheap[0]+self.lheap[0])/2)
        