class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        cur = n

        while cur>1:
            print(f'Checking {cur}')
            if cur in seen:
                return False
            seen.add(cur)
            sum = 0
            while(cur>0):
                add= int(cur%10)
                sum+=add*add
                cur//=10
            cur = sum

        return True