class Solution:
    def firstUniqChar(self, s: str) -> int:
        viable = set()
        seen = set()

        for char in s:
            if char not in seen:
                viable.add(char)
                seen.add(char)
            else:
                if char in viable:
                    viable.remove(char)
        cur = -1
        if len(viable)>0:
            viable = list(viable)
            s = list(s)
            for char in viable:
                if s.index(char)<cur or cur==-1:
                    cur = s.index(char)

        return cur
            

                