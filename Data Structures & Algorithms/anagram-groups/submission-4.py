class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subs = {}

        for word in strs:
            key = "".join(sorted(word))
            subs[key] = subs.get(key, [])
            subs[key].append(word)

        out = []
        for key, val in subs.items():
            out.append(val)

        return out