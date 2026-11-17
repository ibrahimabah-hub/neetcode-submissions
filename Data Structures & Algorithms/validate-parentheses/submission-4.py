class Solution:
    def isValid(self, s: str) -> bool:
        ends = {}
        stack = []
        ends[")"] = "("
        ends["}"] = "{"
        ends["]"] = "["

        cur = 0
        while cur<len(s):
            if s[cur] in ends:
                if stack and ends[s[cur]]==stack.pop():
                    cur+=1
                    continue
                else:
                    return False
            else:
                stack.append(s[cur])
                cur+=1
                continue

        return not stack

