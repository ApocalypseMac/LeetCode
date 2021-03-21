class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = max(nums)
        n = len(nums)
        curr = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                curr = nums[i]
            res = max(res, curr)
        return res