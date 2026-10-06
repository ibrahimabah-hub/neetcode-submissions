class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur = 0
        while cur<len(nums)-1:
            jumps+=1
            jump = cur+nums[cur]
            if jump>=len(nums)-1:
                break
            landing = jump+nums[jump]
            for i in range(1,nums[cur]+1):
                tmpj = cur+i
                tmpl = tmpj+nums[tmpj]
                if tmpl>landing:
                    jump = tmpj
                    landing = tmpl
            cur = jump
            

        return jumps
