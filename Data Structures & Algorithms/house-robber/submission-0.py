class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = {}

        for i in range(len(nums)):
            houses[i] = max(nums[i]+houses.get(i-2, 0), houses.get(i-1, 0))

        return houses[len(nums)-1]