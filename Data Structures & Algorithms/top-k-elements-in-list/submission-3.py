class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        for num in list(collections.Counter(nums).most_common(k)):
            out.append(num[0])
        return out