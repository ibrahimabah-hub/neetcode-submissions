class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1012
        cur = 0
        left = 0
        right = len(nums)-1
        if len(nums)<2:
            return nums
        while(nums[right]==2 and right>0):
            right-=1
        while(nums[left]==0 and left<len(nums)-1):
            left+=1
        while(cur<len(nums)):
            if nums[cur] == 0 and cur>left:
                nums[left], nums[cur] = nums[cur], nums[left]
                left+=1
                continue
            elif nums[cur] == 2 and cur<right:
                nums[right], nums[cur] = nums[cur], nums[right]
                right-=1
                continue

            cur+=1


