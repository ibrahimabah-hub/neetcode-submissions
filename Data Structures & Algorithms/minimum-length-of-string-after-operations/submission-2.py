class Solution:
    def minimumLength(self, s: str) -> int:

        counts = collections.Counter(s)
        
        cur = 0
        for char in list(counts.keys()):
            if counts[char]%2==0 and counts[char]>0:
                cur+=2
            elif counts[char]%2==1:
                cur+=1
            


        return cur
