class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        have = set()

        cur = 0
        while(cur<len(nums)):
            if nums[cur] in have:
                nums.pop(cur)
            else:
                have.add(nums[cur])
                cur+=1

        return len(nums)