#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后K个零
#

# @lc code=start
class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def count(x):
            res = 0
            while x:
                x //= 5
                res += x
            return res
        
        def bisearchl(K):
            lo, hi = 0, 5 * (K + 1)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if count(mid) < K :
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        return bisearchl(K + 1) - bisearchl(K)
        
# @lc code=end

