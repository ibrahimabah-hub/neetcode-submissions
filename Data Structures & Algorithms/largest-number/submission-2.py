from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        out = []
        for num in nums:
            out.append(str(num))
        def compare(int1, int2):
            if int(int1 + int2) > int(int2 + int1):
                return -1
            elif int(int1 + int2) < int(int2 + int1):
                return 1
            else:
                return 0
        output = sorted(out, key=cmp_to_key(compare))
        if output[0]=="0":
            return "0"
        return "".join(output)