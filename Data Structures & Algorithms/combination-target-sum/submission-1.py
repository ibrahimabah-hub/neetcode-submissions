class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        sub = []
        def dfs(i, cur):
            if i>=len(nums) or cur>target:
                if cur == target:
                    result.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i, cur+nums[i])

            sub.pop()
            dfs(i+1, cur)
                
            


        dfs(0, 0)
        return result


            
                
            

            
                