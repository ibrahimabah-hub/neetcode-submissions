class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def bin(num):
            cur = 0
            while num>0:
                cur+=1
                num -= math.pow(2, int(math.log(num, 2)))

            return cur

        res = []
        for i in range(n+1):
            res.append(bin(i))

        return res