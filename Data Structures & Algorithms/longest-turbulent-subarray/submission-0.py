class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        out = 1
        last = None
        cur = 1
        for i in range(1, len(arr)):
            if arr[i]<arr[i-1]:
                if last == "<":
                    cur = 2
                else:
                    cur+=1
                    last = "<"
            elif arr[i]>arr[i-1]:
                if last == ">":
                    cur = 2
                else:
                    cur+=1
                    last = ">"
            else:
                cur = 1
                last = None
            out = max(out, cur)

        return out