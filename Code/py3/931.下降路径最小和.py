#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    from copy import deepcopy
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = deepcopy(A)
        for i in range(m - 2, -1, -1):
            for j in range(n):
                temp = dp[i+1][j]
                if j > 0:
                    temp = min(temp, dp[i+1][j-1])
                if j < n - 1:
                    temp = min(temp, dp[i+1][j+1])
                dp[i][j] += temp
        return min(dp[0])
# @lc code=end

