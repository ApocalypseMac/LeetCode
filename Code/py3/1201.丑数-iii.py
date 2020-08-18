#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] 丑数 III
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            prod = a * b
            while b:
                a = a % b
                a, b = b, a
            return prod // a

        ab, bc, ac = lcm(a, b), lcm(b, c), lcm(a, c)
        abc = lcm(ab, c)

        def count(num):
            return num // a + num // b + num // c - num // ab - num // bc - num // ac + num // abc

        lo, hi = 1, min(a, b, c) * n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            temp = count(mid)
            if temp < n:
                lo = mid + 1
            else:
                hi = mid
        return lo
            
        
# @lc code=end

