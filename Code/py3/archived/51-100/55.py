class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxlen = 0
        i = 0
        while i <= maxlen and i < len(nums):
            maxlen = max(maxlen, i + nums[i])
            i += 1
            if maxlen >= len(nums) - 1:
                return True
        return False