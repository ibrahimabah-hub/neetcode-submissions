class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char, 0)+1
        window = {}
        l = 0
        r = len(s)
        h_t = 0
        n_t = len(need)
        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            
            window[s[i]] = window.get(s[i], 0) + 1

            if s[i] in need and window[s[i]] == need[s[i]]:
                h_t += 1

            while h_t == n_t:
                if (i - l + 1)< resLen:
                    res = [l,i]
                    resLen = (i - l +1)

                window[s[l]]-=1
                if s[l] in need and window[s[l]]< need[s[l]]:
                    h_t-=1
                l+=1
        l, r = res
        return s[l:r+1] if resLen != (float("infinity")) else ""
            


        
                    
                
