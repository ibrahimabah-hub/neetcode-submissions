class Solution:
    def checkValidString(self, s: str) -> bool:
        burn = []
        l = []

        for i in range(len(s)):
            if s[i]=="(":
                l.append(i)
            if s[i]=="*":
                burn.append(i)
            if s[i]==")":
                if len(l)>0:
                    l.pop()
                elif len(burn)>0:
                    burn.pop()
                else:
                    return False

        while(len(l)>0):
            if len(burn)<1 or l[-1]>burn[-1]:
                return False
            else:
                burn.pop()
                l.pop()

        return True