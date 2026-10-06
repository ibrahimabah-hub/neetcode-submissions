class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        cur = nums[0]
        res = cur
        for i in range(1, len(nums)):
            cur = max(nums[i], cur+nums[i])
            res = max(res, cur)


        return res