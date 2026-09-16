class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = -1
        l = 0
        r = len(nums)-1

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        while r>l+1:
            x = (r+l)//2
            if nums[r] == target:
                return r
            if nums[x] == target:
                ind = x
                break
            if nums[x] < target:
                if nums[r] < target and nums[r] > nums[x]:
                    r = x
                else:
                    l = x
            if nums[x] > target:
                if nums[l] > target and nums[l]< nums[x]:
                    l = x
                else:
                    r = x
        
        return ind
                