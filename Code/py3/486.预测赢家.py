#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#

# @lc code=start
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True
        dp = [[0] * n for _ in range(n)] # max point diff by P1
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # choose left/right boundary
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        #print(dp)
        return dp[0][-1] >= 0
# @lc code=end

