class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        totals = []
        nums.sort()
        checked = {}
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            l = nums[i]
            r = nums[k]+nums[j]
            while(j<k):
                if l+r == 0:
                    total = [nums[i], nums[j], nums[k]]
                    if total not in totals:
                        totals.append(total)
                    k-=1
                if l<0-r:
                    if(l<0-(nums[k]+nums[k-1])):
                        break
                    j+=1
                if l>0-r:
                    k-=1
                r = nums[k]+nums[j]    
                
        return totals

