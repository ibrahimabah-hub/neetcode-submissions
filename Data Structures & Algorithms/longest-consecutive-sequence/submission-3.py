class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        for num in nums:
            numbers.add(num)
        max_len = 0
        checked = set()
        for i in nums:
            if i not in checked:
                checked.add(i)
            else:
                continue
            length = 1
            j = i+1
            while j in numbers:
                length+=1
                if j not in checked:
                    checked.add(j)
                j+=1
            if length>max_len:
                max_len = length
        return max_len