class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = {}
        for char in s:
            counts1[char] = 1+counts1.get(char, 0)

        counts2 = {}
        for char in t:
            counts2[char] = 1+counts2.get(char, 0)

        return counts1==counts2