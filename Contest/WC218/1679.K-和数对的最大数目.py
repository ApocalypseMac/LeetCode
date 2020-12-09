class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, n - 1
        res = 0
        while lo < hi:
            sum_ = nums[lo] + nums[hi]
            if sum_ == k:
                res += 1
                lo += 1
                hi -= 1
            elif sum_ > k:
                hi -= 1
            else:
                lo += 1
        return res