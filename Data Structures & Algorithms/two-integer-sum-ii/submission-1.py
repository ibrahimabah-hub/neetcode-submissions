class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)-1
        l = 0
        
        while l<r:
            x = target-numbers[l]
            if x == numbers[r]:
                break
            if x < numbers[r]:
                r-=1
                continue
            else:
                l+=1
        return [l+1,r+1]