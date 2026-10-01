class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = 1
        cur_min = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                cur_min, cur_max = 1, 1
                continue
            
            tmp = cur_max * nums[i]
            cur_max = max(cur_min*nums[i], cur_max*nums[i], nums[i])
            cur_min = min(tmp, cur_min*nums[i], nums[i])
            res = max(res, cur_max)
        
        return res

