import heapq as hq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = points
        heap = []
        points = {}
        res = []
        for i in nums:
            dist = math.sqrt(math.pow((i[0]), 2) + math.pow((i[1]), 2))
            hq.heappush(heap, dist)
            if dist not in points:
                points[dist] = [i]
            else:
                points[dist].append(i)
        for i in range(k):
            res.append(points[hq.heappop(heap)].pop())

        return res