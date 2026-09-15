import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 0
        r = piles[-1]
        cur = 0
        while l<r-1:
            k = (l+r)//2
            hours = 0
            for i in range(len(piles)):
                hours+=(math.ceil(piles[i]/k))
            print(f"{k} bananas takes {hours} hours")
            if hours<=h:
                r = k
            else:
                l = k
        return math.ceil((l+r)/2)
