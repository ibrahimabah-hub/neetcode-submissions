class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        cur = ""
        for i in range(len(s)):
            r = i+1
            while(r in range(len(s)) and s[r]==s[i]):
                r+=1
            l = i-1
            cur = s[i:r]
            while(l in range(len(s)) and r in range(len(s))):
                if s[l] == s[r]:
                    cur = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
            if len(cur)> len(longest):
                longest = cur
        
        return longest