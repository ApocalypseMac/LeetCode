#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def num(s):
            res = [0] * 2
            for ch in s:
                if ch == '0':
                    res[0] += 1
                else:
                    res[1] += 1
            return res
        nums = []
        for s in strs:
            freq = num(s)
            if freq[0] <= m and freq[1] <= n:
                nums.append(freq)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for freq in nums:
            for i in range(m, freq[0]-1, -1): # 0-1 backpack: reverse order
                for j in range(n, freq[1]-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-freq[0]][j-freq[1]])
        return dp[-1][-1]

# @lc code=end

