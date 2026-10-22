class Solution:
    def mySqrt(self, x: int) -> int:
        cur = 0

        while(cur*cur <= x):
            cur+=1
        
        return cur-1