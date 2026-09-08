class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = defaultdict(list)
        for word in strs:
            sort = "".join(sorted(word))
            sets[sort].append(word)
        return list(sets.values())