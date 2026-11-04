class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = set()
        cur = 0
        while(cur*cur)<=c:
            nums.add(cur*cur)
            cur+=1

        for num in nums:
            if c-num in nums:
                return True

        return False