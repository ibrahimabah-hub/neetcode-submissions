class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = 0
        
        for i in range(len(digits)):
            cur*=10
            cur+=digits[i]
        cur+=1
        res = []
        while cur>0:
            res.insert(0, cur%10)
            cur = cur//10

        return res