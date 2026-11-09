class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = 0
        for i in range(len(nums)):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                nums[i]+=nums[i]
                nums[i+1] = 0
            if nums[i]==0:
                zeros+=1
        print(nums)
        cur = 0
        while(cur<len(nums)):
            print(zeros)
            if nums[cur]==0 and zeros>=1:
                nums.pop(cur)
                nums.append(0)
                zeros-=1
                continue
            cur+=1

        return nums

