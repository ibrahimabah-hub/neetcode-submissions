class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if char not in chars:
                chars[char]=1
            else:
                chars[char]+=1
        for char in t:
            if char not in chars:
                print('Not in set')
                return False
            chars[char]-=1
            if chars[char]<0:
                print('Too many letters')
                return False
        x = chars.values()
        for char in x:
            if char !=0:
                print('Leftover letters')
                print(char)
                return False
        return True