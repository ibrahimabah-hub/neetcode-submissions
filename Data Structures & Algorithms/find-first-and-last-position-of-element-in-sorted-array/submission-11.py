class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)
        if not nums or target<nums[l] or target>nums[r-1]:
            return[-1, -1]
        while(l<r):
            idx = (l+r)//2
            if r-l<2 and nums[l]!=target:
                return[-1,-1]
            if nums[idx]==target:
                break
            if nums[idx]<target:
                l = idx
            else:
                r = idx
        
        idx = (l+r)//2
        start = idx
        while start>0 and nums[start-1]==target:
            start -= 1
        end = idx
        while end<len(nums)-1 and nums[end+1]==target:
            end+=1
        
        return [start, end]
