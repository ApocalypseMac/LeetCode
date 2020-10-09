class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: -x)
        n = len(nums)
        j = 0
        for i in range(1000, -1, -1):
            while j < n and i <= nums[j]:
                j += 1
            if i == j:
                return i
        return -1
            
            