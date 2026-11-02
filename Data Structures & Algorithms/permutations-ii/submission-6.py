class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        sub = []

        def dfs(i):
            if i>=len(nums):
                cur = []
                for num in sub:
                    cur.append(nums[num])
                if cur not in res:
                    res.append(cur)
                return

            for x in range(len(nums)):
                if x not in sub:
                    sub.append(x)
                    dfs(i+1)
                    sub.pop()
        

        dfs(0)
        
        return(res)