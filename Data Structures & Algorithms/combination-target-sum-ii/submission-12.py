class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        sub = []
        candidates.sort()
        def dfs(i, cur):
            checked = set()
            if i>= len(candidates) or cur>=target:
                if cur==target and sub.copy() not in result:
                    result.append(sub.copy())
                return
            num = candidates[i]
            checked.add(num)
            sub.append(num)
            dfs(i+1, cur+num)
            sub.pop()
            j = i+1
            while(j<len(candidates) and candidates[j]==num):
                j+=1
            dfs(j, cur)


        dfs(0, 0)
        return result