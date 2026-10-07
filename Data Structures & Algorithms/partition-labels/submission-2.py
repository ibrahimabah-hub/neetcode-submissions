class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = [i]
            else:
                count[s[i]].append(i)
        
        arr = set()

        cur = -1

        for i in range(len(s)):
            if s[i] not in arr:
                arr.add(s[i])
            if i==count[s[i]][-1]:
                arr.remove(s[i])
            if len(arr)<1:
                res.append(i-cur)
                cur = i

        return res
            