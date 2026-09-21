class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = nums[0]
        ii = nums[nums[0]]
        while i!=ii:
            i = nums[i]
            ii = nums[nums[ii]]

        ni = nums[0]
        i = nums[i]
        while ni != i:
            ni = nums[ni]
            i = nums[i]

        return i