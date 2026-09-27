class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x>0:
                return 1
            if x<0:
                return -1
            return 0
        status = 1
        for num in nums:
            if num==0:
                return 0
            status = status*signFunc(num)
        return status