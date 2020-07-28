class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = 2
        while hi ** 2 <= x:
            lo = hi
            hi *= 2
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if mid ** 2 <= x:
                lo = mid
            else:
                hi = mid
        return lo