#
# @lc app=leetcode.cn id=5490 lang=python3
#
# [5490] 吃掉 N 个橘子的最少天数
#

# @lc code=start
class Solution:
    def minDays(self, n: int) -> int:
        self.dp = {0: 1, 1: 1}
        def helper(n):
            if n in self.dp:
                return self.dp[n]
            temp1 = helper(n // 2) + 1 + n % 2
            temp2 = helper(n // 3) + 1 + n % 3
            res = min(temp1, temp2)
            self.dp[n] = res
            return res
        return helper(n)
# @lc code=end

