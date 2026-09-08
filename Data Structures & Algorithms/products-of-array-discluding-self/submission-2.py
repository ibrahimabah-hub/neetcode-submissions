class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prearr = [0]*len(nums)
        suffix = [1]*len(nums)
        if len(prearr)<2:
            return nums
        prearr[0]=1
        for i in range(len(nums)-1):
            prearr[i+1]= prearr[i]*nums[i]
        for i in range(len(nums)-1):
            j = len(nums)-i-1
            suffix[j-1]=nums[j]*suffix[j]
        result = [1]*len(nums)
        for i in range(len(result)):
            result[i] = suffix[i] * prearr[i]
        return result
