class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            val = nums[i]
            if target-val in vals:
                return([vals[target-val], i])
            if nums[i] not in vals:
                vals[nums[i]] = i