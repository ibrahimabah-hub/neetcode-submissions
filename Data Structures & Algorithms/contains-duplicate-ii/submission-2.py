class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        counts = {}

        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], [])
            counts[nums[i]].append(i)
            if len(counts[nums[i]])>1 and abs(counts[nums[i]][-1]-counts[nums[i]][-2])<=k:
                return True
        print(counts)
        return False
