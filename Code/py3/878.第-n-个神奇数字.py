#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#

# @lc code=start
class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def lcm(a, b):
            prod = a * b
            while b:
                a = a % b
                a, b = b, a
            return prod // a

        # count of magic numbers <= num
        def count(num, a, b, l):
            return num // a + num // b - num // l

        if A < B:
            A, B = B, A
        if A % B == 0:
            return (N * B) % (10 ** 9 + 7)
        l = lcm(A, B)
        #print(l)
        lo, hi = B, N * B 
        while lo < hi:
            mid = lo + (hi - lo) // 2
            temp = count(mid, A, B, l)
            #print(temp, mid, l)
            if temp >= N:
                hi = mid
            else:
                lo = mid + 1
        return lo % (10 ** 9 + 7)

        
# @lc code=end

