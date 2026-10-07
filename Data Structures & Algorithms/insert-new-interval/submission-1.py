class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        rep = newInterval

        idx = 0

        while(idx<len(intervals)):
            cur = intervals[idx]
            if cur[1]<rep[0]:
                idx+=1
                continue
            if rep[1]<cur[0]:
                intervals.insert(idx, rep)
                break
            
            if rep[0]<=cur[1]:
                rep[0] = min(cur[0], rep[0])
                rep[1] = max(rep[1], cur[1])
                intervals.pop(idx)
                continue

        if idx>=len(intervals):
            intervals.append(rep)

        return intervals
        
            