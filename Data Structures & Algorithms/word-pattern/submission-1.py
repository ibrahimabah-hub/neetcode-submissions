class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pIdx = {}
        wIdx = {}
        words = s.split()
        if len(words)!= len(pattern):
            return False
        for i in range(len(words)):
            pIdx[pattern[i]] = pIdx.get(pattern[i], words[i])
            wIdx[words[i]] = wIdx.get(words[i], pattern[i])
            if pIdx[pattern[i]] != words[i] or wIdx[words[i]]!=pattern[i]:
                return False

        return True