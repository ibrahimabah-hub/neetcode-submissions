class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        cur = str1[0]
        index = 1
        def divide(s, t):
            test = t
            while(len(test)<len(s)):
                test = test + t
            if s==test:
                return True
            return False

        while index<=len(str1) and index<=len(str2):
            if divide(str1, cur) and divide(str2, cur):
                res = cur
            print(cur)
            index+=1
            cur = str1[:index]

        return res