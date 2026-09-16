class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minimum = min(nums[l], nums[r])
        while(r>l+1):
            ind = (r+l)//2
            if(nums[ind] < minimum):
                ind_m = ind
                minimum = nums[ind]

            if nums[ind]>nums[r]:
                l = ind
            else:
                r = ind
        
        return minimum
            
