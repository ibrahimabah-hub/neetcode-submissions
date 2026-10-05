class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if len(arr)<2:
                return arr
            
            l = merge(arr[:len(arr)//2])
            r = merge(arr[len(arr)//2:])
            res = []
            while(l and r):
                if l[0]<r[0]:
                    res.append(l.pop(0))
                else:
                    res.append(r.pop(0))
            while l:
                res.append(l.pop(0))
            while r:
                res.append(r.pop(0))

            return res

        return merge(nums)

