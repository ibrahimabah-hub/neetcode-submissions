class Solution:
    def romanToInt(self, s: str) -> int:
        l = 0
        out = 0
        while(l<len(s)):
            char = s[l]
            if char=="I":
                if l<len(s)-1:
                    if s[l+1]=="X":
                        out+=9
                        l+=2
                        continue
                    elif s[l+1]=="V":
                        out+=4
                        l+=2
                        continue
                out+=1
            elif char=="V":
                out+=5
            elif char == "X":
                if l<len(s)-1:
                    if s[l+1]=="L":
                        out+=40
                        l+=2
                        continue
                    elif s[l+1]=="C":
                        out+=90
                        l+=2
                        continue
                out+=10
            elif char =="L":
                out+=50
            elif char=="C":
                if l<len(s)-1:
                    if s[l+1]=="D":
                        out+=400
                        l+=2
                        continue
                    elif s[l+1]=="M":
                        out+=900
                        l+=2
                        continue
                out+=100
            elif char=="D":
                out+=500
            elif char=="M":
                out+=1000
            l+=1

        return out