class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        sub = []
        nums.sort()
        def dfs(i):
            if i>=len(nums):
                if sub.copy() not in res:
                    res.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            j = i+1
            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            dfs(j)

        dfs(0)
        return res