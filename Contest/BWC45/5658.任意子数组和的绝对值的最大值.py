class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        pmax = 0
        pmin = 0
        p = 0
        for num in nums:
            p += num
            res = max(res, abs(p - pmax), abs(p - pmin))
            pmax = max(pmax, p)
            pmin = min(pmin, p)
        return res