class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        q = []
        for i in range(len(nums)):
            if i-k in q:
                q.remove(i-k)
            while len(q)>0 and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            if i>=k-1:
                maxes.append(nums[q[0]])
        return maxes