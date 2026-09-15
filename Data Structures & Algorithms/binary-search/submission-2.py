class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        if nums[0]== target:
            return 0
        while l<r-1:
            idx = (r+l)//2
            if nums[idx] == target:
                return idx
            if nums[idx] < target:
                l = idx
            else:
                r = idx
        return -1