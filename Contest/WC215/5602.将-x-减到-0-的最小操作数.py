class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1
        n = len(nums)
        lo, hi = 0, n - 1
        temp = 0
        res = 10 ** 10
        while lo < n and temp < x:
            temp += nums[lo]
            lo += 1
        if temp == x:
            res = lo
        while lo >= 0:
            lo -= 1
            temp -= nums[lo]
            while temp < x:
                temp += nums[hi]
                hi -= 1
            if temp == x:
                res = min(res, lo + (n - 1) - hi)
        if res < 10 ** 10:
            return res
        else:
            return -1
            
        