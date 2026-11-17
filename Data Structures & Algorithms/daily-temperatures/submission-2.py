class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            cur = temperatures[i]
            if i<len(temperatures)-1:
                while(stack):
                    tmp = stack.pop()
                    if cur>=temperatures[tmp]:
                        continue
                    else:
                        stack.append(tmp)
                        break
                if stack:
                    res[i] = tmp-i
            stack.append(i)

        return res
