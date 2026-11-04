class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = set()
        cur = 0
        while(cur*cur)<=c:
            
            nums.add(cur*cur)
            if c-(cur*cur) in nums:
                return True
            cur+=1

        return False