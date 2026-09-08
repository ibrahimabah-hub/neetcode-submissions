class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = count.get(i, 0)+1
        for n, c in count.items():
            freq[c].append(n)
        answer = []
        for i in range(len(freq)):
            for j in freq[len(freq)-(i+1)]:
                answer.append(j)
                if len(answer)==k:
                    return answer