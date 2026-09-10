class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        max_len = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = i
                word = s[left:i+1]
            else:
                left = max(letters[s[i]]+1, left)
                letters[s[i]] = i
                word = s[left:min(len(s),i+1)]
            if len(word)>max_len:
                print(word)
                max_len = len(word)
        
        return max_len