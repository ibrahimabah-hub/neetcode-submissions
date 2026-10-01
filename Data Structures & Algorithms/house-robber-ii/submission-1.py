class Solution:
    def rob(self, nums: List[int]) -> int:
        withE = {}

        withZ = {}
        if len(nums)<2:
            return nums[0]
        for i in range(len(nums)):
            if i>0:
                withE[i] = max(withE.get(i-2, 0)+nums[i], withE.get(i-1, 0))
            if i<len(nums)-1:
                withZ[i] = max(withZ.get(i-2, 0)+nums[i], withZ.get(i-1, 0))

        return max(withE[len(nums)-1], withZ[len(nums)-2])
