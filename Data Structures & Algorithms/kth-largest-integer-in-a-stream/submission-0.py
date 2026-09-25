class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums.sort()
        self.nums = self.nums[-k:]
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        self.nums = self.nums[-self.k:]
        return(self.nums[0])
