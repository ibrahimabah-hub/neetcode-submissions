class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        out = 0

        g.sort()
        s.sort()

        cur = 0

        while(cur<len(g) and cur<len(s)):
            if g[cur]<=s[cur]:
                out+=1
                cur+=1
            else:
                s.pop(cur)

        return out