class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def poss(sub):
            if len(sub)==len(nums):
                res.append(sub.copy())
                return
            for num in nums:
                if num not in sub:
                    tmp = sub.copy()
                    tmp.append(num)
                    poss(tmp)
            

                    
        poss([])

        return res

