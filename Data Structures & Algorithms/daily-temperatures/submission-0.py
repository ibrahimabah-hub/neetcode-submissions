class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        sort = []
        output = [0] * len(temp)
        for i in range(len(temp)):
            while(len(sort)>0 and temp[i]>temp[sort[-1]] ):
                j = sort.pop()
                output[j] = i-j
            sort.append(i)
            
        return output
            