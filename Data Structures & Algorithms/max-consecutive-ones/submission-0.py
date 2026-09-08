class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        cur_max = 0
        for i in range(len(nums)):
            if nums[i]==1:
                cur_max+=1
                if cur_max>max:
                    max = cur_max
                continue
            cur_max=0
        return max

        