#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除与获得点数
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        count = [0] * (max(nums) + 1)
        for num in nums:
            count[num] += num
        dp = [0] * (max(nums) + 1)
        dp[1] = count[1]
        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + count[i])
        return dp[-1]
# @lc code=end

