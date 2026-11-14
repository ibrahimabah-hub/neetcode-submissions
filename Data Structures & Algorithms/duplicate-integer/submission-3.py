class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set()
        for num in nums:
            if num in nums1:
                return True
            nums1.add(num)
        return False