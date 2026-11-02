class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = nums[0]
        times = 0

        for i in range(len(nums)):
            if nums[i]==cur:
                times+=1
            else:
                times-=1
            if times<0:
                cur = nums[i]
                times = 1

        return cur