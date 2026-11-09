class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        cur = num[0]
        while(len(num)>1):
            cur*=10
            cur+=num[1]
            num.pop(0)
        #print(cur)
        cur+=k
        out = []
        out.append(int(cur%10))
        cur//=10
        while cur>0:
            out.insert(0, int(cur%10))
            cur//=10

        return out