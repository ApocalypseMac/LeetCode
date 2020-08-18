#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # similar with LC300
        n = len(envelopes)
        if n <= 1:
            return n
        envelopes.sort(key = lambda x: (x[1], -x[0])) # avoid put same height
        dp = [0 for _ in range(n)]
        dp[0] = envelopes[0][0]
        def bisearch(lo, hi, n):
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if dp[mid] < n:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        res = 1
        for i in range(1, n):
            temp = envelopes[i][0]
            if temp > dp[res - 1]:
                dp[res] = temp
                res += 1
            else:
                index = bisearch(0, res, temp)
                dp[index] = temp
        return res

        
# @lc code=end

