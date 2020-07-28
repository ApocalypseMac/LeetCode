class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -2147483647 # INT_MIN
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else: # at first time sum (maxsum) = nums[0]
                sum = num
            maxsum = max(sum, maxsum)
        return maxsum